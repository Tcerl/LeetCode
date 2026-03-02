# 🌶️ FLASK & BACKEND - ÔN THI PHỎNG VẤN

---

## 1. FLASK CƠ BẢN

### 1.1 App Factory Pattern
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="development"):
    """Application factory - tạo app theo môi trường"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Khởi tạo extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Đăng ký blueprints
    from .routes.auth import auth_bp
    from .routes.api import api_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    return app
```

> **🎯 Dùng khi nào?**
> - Tránh circular imports khi app lớn
> - Cho phép tạo nhiều instance khác nhau (testing, prod, dev)
> - Đây là **best practice** cho Flask production apps

---

### 1.2 Blueprint Pattern
```python
# routes/auth.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    # validate credentials
    return jsonify({"token": generate_token()})

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()  # decorator bảo vệ route
def logout():
    return jsonify({"message": "Logged out"})
```

> **🎯 Dùng khi nào?**
> - Chia code theo feature modules
> - Mỗi blueprint là 1 mini-app: auth, users, products, orders

---

## 2. REST API DESIGN

### 2.1 Chuẩn RESTful
```python
# RESTful Resource: /api/v1/users
GET    /users          -> list users
GET    /users/{id}     -> get user by id
POST   /users          -> create user
PUT    /users/{id}     -> update (full replace)
PATCH  /users/{id}     -> update (partial)
DELETE /users/{id}     -> delete

# Status codes quan trọng
200 OK                 # Success GET, PUT, PATCH
201 Created            # Success POST
204 No Content         # Success DELETE
400 Bad Request        # Client input error
401 Unauthorized       # Chưa authenticate
403 Forbidden          # Đã auth nhưng không có quyền
404 Not Found          # Resource không tồn tại
409 Conflict           # Duplicate resource
422 Unprocessable      # Validation failed
429 Too Many Requests  # Rate limit
500 Internal Server    # Server error
```

### 2.2 Flask API với validation
```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError

class UserCreateSchema(Schema):
    name = fields.Str(required=True, validate=lambda n: len(n) >= 2)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    age = fields.Int(validate=lambda a: 0 < a < 120)

users_bp = Blueprint("users", __name__)
schema = UserCreateSchema()

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 422

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "email": user.email}), 201

@users_bp.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404
```

---

## 3. SQLALCHEMY ORM

### 3.1 Model Definition
```python
from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    posts = db.relationship("Post", back_populates="author", lazy="dynamic")
    profile = db.relationship("Profile", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User {self.email}>"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    author = db.relationship("User", back_populates="posts")
```

### 3.2 Queries
```python
# Basic queries
user = User.query.get(1)                          # by PK
user = User.query.filter_by(email="a@b.com").first()
users = User.query.filter(User.is_active == True).all()

# Complex queries
from sqlalchemy import and_, or_, desc, func

users = (User.query
    .filter(and_(User.is_active == True, User.age > 18))
    .order_by(desc(User.created_at))
    .limit(20)
    .offset(0)
    .all())

# JOIN
result = (db.session.query(User, Post)
    .join(Post, User.id == Post.author_id)
    .filter(User.is_active == True)
    .all())

# Aggregate
count = db.session.query(func.count(User.id)).scalar()
avg_age = db.session.query(func.avg(User.age)).scalar()

# Pagination
page = User.query.paginate(page=1, per_page=20, error_out=False)
# page.items, page.total, page.pages, page.has_next
```

### 3.3 Lazy Loading vs Eager Loading
```python
# LAZY (N+1 problem!)
users = User.query.all()
for user in users:
    print(user.posts.all())  # query thêm DB cho MỖI user → N+1!

# EAGER (joinedload) - 1 query duy nhất
from sqlalchemy.orm import joinedload
users = User.query.options(joinedload(User.posts)).all()
for user in users:
    print(user.posts)  # không query thêm

# SUBQUERY load - tốt cho one-to-many với nhiều records
users = User.query.options(subqueryload(User.posts)).all()
```

> **🎯 N+1 Problem quan trọng khi phỏng vấn!**
> - Nếu có 100 users, lazy load sẽ tạo 101 queries (1 cho users + 100 cho posts)
> - **Giải pháp**: Dùng `joinedload()` hoặc `subqueryload()`

---

## 4. AUTHENTICATION

### 4.1 JWT Authentication
```python
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
import bcrypt

# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not bcrypt.checkpw(
        data["password"].encode(), user.password_hash
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=user.id,
        additional_claims={"role": user.role}
    )
    return jsonify({"access_token": token})

# Protected route
@api_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user.to_dict())
```

### 4.2 Role-based Access Control
```python
from functools import wraps
from flask_jwt_extended import get_jwt

def require_role(*roles):
    """Decorator check role"""
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") not in roles:
                return jsonify({"error": "Insufficient permissions"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@admin_bp.route("/users", methods=["GET"])
@require_role("admin", "superadmin")
def list_all_users():
    pass
```

> **🎯 Dùng khi nào?**
> - **JWT**: Stateless auth, mobile apps, microservices
> - **Session**: Stateful, web apps, khi cần revoke ngay lập tức
> - **JWT + Refresh Token**: Balance giữa security và UX

---

## 5. WEBSOCKETS VỚI FLASK-SOCKETIO

```python
from flask_socketio import SocketIO, emit, join_room, leave_room

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("connect")
def handle_connect():
    print(f"Client connected: {request.sid}")

@socketio.on("join_room")
def handle_join(data):
    room = data["room"]
    join_room(room)
    emit("status", {"msg": f"Joined room {room}"})

@socketio.on("send_message")
def handle_message(data):
    room = data["room"]
    # Broadcast tới tất cả người trong room
    emit("receive_message", data, room=room)

@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")
```

> **🎯 Dùng khi nào?**
> - **Chat apps, live notifications**: Dùng WebSocket (bi-directional)
> - **Server → Client only**: Dùng SSE (Server-Sent Events) đơn giản hơn
> - Trong dự án **Viet Kiosk** của bạn: Real-time patient updates

---

## 6. MIDDLEWARE & REQUEST HOOKS

```python
# Before/After request hooks
@app.before_request
def log_request():
    """Chạy trước mọi request"""
    g.start_time = time.time()
    logger.info(f"{request.method} {request.path}")

@app.after_request
def log_response(response):
    """Chạy sau mọi request"""
    elapsed = time.time() - g.start_time
    logger.info(f"Response {response.status_code} in {elapsed:.3f}s")
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Cleanup DB session sau mỗi request"""
    db.session.remove()

# Custom middleware
class RateLimitMiddleware:
    def __init__(self, app, requests_per_minute=60):
        self.app = app
        self.limit = requests_per_minute
        self.requests = {}

    def __call__(self, environ, start_response):
        ip = environ.get("REMOTE_ADDR")
        # check rate limit logic
        return self.app(environ, start_response)
```

---

## 7. ERROR HANDLING & LOGGING

```python
import logging
from logging.handlers import RotatingFileHandler

# Cấu hình logging
def setup_logging(app):
    handler = RotatingFileHandler(
        "app.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

# Global error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "path": request.path}), 404

@app.errorhandler(500)
def server_error(e):
    app.logger.error(f"Server error: {e}", exc_info=True)
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    app.logger.error(f"Unhandled exception: {e}", exc_info=True)
    return jsonify({"error": "Something went wrong"}), 500
```

---

## 8. CELERY - BACKGROUND TASKS

```python
from celery import Celery

celery = Celery(app.name)
celery.config_from_object(app.config)

@celery.task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    """Background task gửi email"""
    try:
        send_email(recipient, subject, body)
    except Exception as exc:
        # Retry sau 60s
        raise self.retry(exc=exc, countdown=60)

@celery.task
def process_data_migration(migration_id):
    """Long-running task migrate data"""
    migration = Migration.query.get(migration_id)
    migration.status = "running"
    db.session.commit()

    try:
        # Process trong background
        migrate_products(migration)
        migrate_orders(migration)
        migration.status = "completed"
    except Exception as e:
        migration.status = "failed"
        migration.error = str(e)
    finally:
        db.session.commit()

# Gọi task
result = send_email_task.delay("user@email.com", "Hi", "Hello")
result.id  # task ID để track
```

> **🎯 Dùng khi nào?**
> - Gửi email, SMS (không block request)
> - Data migration (trong dự án eCommerce Migration của bạn)
> - Report generation, file processing
> - Scheduled tasks (kết hợp Celery Beat)

---

## ✅ CHECKLIST FLASK/BACKEND

- [ ] Giải thích App Factory pattern và tại sao dùng nó
- [ ] N+1 problem và cách fix với eager loading
- [ ] JWT vs Session auth - khi nào dùng cái nào
- [ ] Thiết kế RESTful API endpoints chuẩn
- [ ] Celery task async cho long-running jobs
- [ ] WebSocket vs HTTP - khi nào dùng cái nào
- [ ] Role-based access control
