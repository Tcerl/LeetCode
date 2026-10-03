# ✅ Checklist & Hướng Dẫn Thực Hành Chi Tiết Bài Tập Flask (FL-01 → FL-04)

> **Mục tiêu:** Cảm nhận và phân tích sâu sắc sự khác biệt giữa triết lý **Micro-framework (Flask)** và **Batteries-included (Django)**. Hiểu rõ cách Flask quản lý Context (`app_context`, `request_context`), SQLAlchemy Session Lifecycle, Blueprint Architecture và Containerization với Docker.

---

## 📌 Danh Sách Bài Tập
- [ ] **FL-01 — Flask Thuần & Low-level Routing** (Tuần 9)
- [ ] **FL-02 — Tích hợp Flask-SQLAlchemy & ORM Mapping** (Tuần 10)
- [ ] **FL-03 — Modular Design với Flask Blueprints & Factory Pattern** (Tuần 10)
- [ ] **FL-04 — Dockerization & Container Execution** (Tuần 11)

---

## 📘 HƯỚNG DẪN THỰC HÀNH CHI TIẾT & GIẢI THÍCH CHUYÊN SÂU

### 1. FL-01 — Flask Thuần & Low-level Routing
#### 🔬 Giải thích chuyên sâu:
- **Triết lý Micro-framework:** Flask chỉ cung cấp WSGI Wrapper (dựa trên Werkzeug) và Template Engine (Jinja2). Tất cả các thành phần khác như Database ORM, Form Validation, Authentication, Migration đều phải tự chọn thư viện ngoài và gắn vào.
- **Application Context vs Request Context:**
  - Flask sử dụng Thread-local (hoặc ContextVar trong Python async) để quản lý state toàn cục nhưng biến đổi theo thread/request.
  - `g`: Application context object, tồn tại trong suốt một request lifecycle để lưu trữ dữ liệu tạm (VD: kết nối DB, user info).
  - `request`: Request context object đại diện cho HTTP Request hiện tại (headers, query params, body JSON).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Khởi tạo môi trường & Cài đặt:**
   ```bash
   mkdir flask_app && cd flask_app
   python -m venv venv
   source venv/bin/activate
   pip install flask
   ```
2. **Viết REST API bằng Flask thuần không dùng ORM (`app.py`):**
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   # In-memory storage giả lập DB
   posts_db = [
       {"id": 1, "title": "Flask Basics", "content": "Microframework in Python"},
       {"id": 2, "title": "Django vs Flask", "content": "Batteries vs Custom"}
   ]

   @app.route('/api/posts', methods=['GET'])
   def get_posts():
       return jsonify(posts_db), 200

   @app.route('/api/posts', methods=['POST'])
   def create_post():
       data = request.get_json()
       if not data or 'title' not in data or 'content' not in data:
           return jsonify({"error": "Bad Request: Missing title or content"}), 400

       new_post = {
           "id": len(posts_db) + 1,
           "title": data['title'],
           "content": data['content']
       }
       posts_db.append(new_post)
       return jsonify(new_post), 201

   if __name__ == '__main__':
       app.run(debug=True, port=5000)
   ```
3. **Chạy & Ghi chú tự đánh giá:**
   - Chạy `python app.py` và dùng cURL kiểm tra `GET` và `POST`.
   - **Ghi chú:** Thống kê những gì Django làm sẵn nhưng Flask phải tự viết: Parsing JSON body, Error Handler 400/500, Response status code formatting, DB Connection management.

---

### 2. FL-02 — Tích Hợp Flask-SQLAlchemy & ORM Mapping
#### 🔬 Giải thích chuyên sâu:
- **SQLAlchemy Unit of Work & Session Pattern:**
  - Đằng sau Flask-SQLAlchemy là SQLAlchemy - ORM mạnh nhất Python.
  - Khác với Django ORM (Active Record Pattern - nơi object tự gọi `.save()`), SQLAlchemy dùng **Data Mapper & Unit of Work Pattern**.
  - Các thay đổi dữ liệu được theo dõi trong một `db.session`. Khi gọi `db.session.add(obj)`, object chỉ được đưa vào trạng thái tracking (Pending). Dữ liệu chỉ thực sự được flush và ghi xuống SQL Database khi gọi `db.session.commit()`.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Cài đặt Flask-SQLAlchemy:**
   ```bash
   pip install flask-sqlalchemy
   ```
2. **Khai báo Schema & Tích hợp (`app_orm.py`):**
   ```python
   from flask import Flask, request, jsonify
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   db = SQLAlchemy(app)

   class Post(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(200), nullable=False)
       content = db.Column(db.Text, nullable=False)

       def to_dict(self):
           return {"id": self.id, "title": self.title, "content": self.content}

   with app.app_context():
       db.create_all()

   @app.route('/api/posts', methods=['GET'])
   def get_posts():
       posts = Post.query.all()
       return jsonify([p.to_dict() for p in posts]), 200

   @app.route('/api/posts', methods=['POST'])
   def create_post():
       data = request.get_json()
       new_post = Post(title=data['title'], content=data['content'])
       db.session.add(new_post)
       db.session.commit()  # Flush & Execute Transaction
       return jsonify(new_post.to_dict()), 201
   ```
3. **So sánh Cú pháp Query:**
   - Django: `Post.objects.filter(title__icontains='Flask')`
   - Flask-SQLAlchemy: `Post.query.filter(Post.title.like('%Flask%')).all()`

---

### 3. FL-03 — Blueprint hóa & Application Factory Pattern
#### 🔬 Giải thích chuyên sâu:
- **Application Factory Pattern (`create_app()`):** Tránh việc khởi tạo instance `app = Flask(__name__)` ở quy mô global. Việc khởi tạo app trong một hàm factory cho phép tạo ra nhiều instance app khác nhau cho Testing (với in-memory DB) hoặc Production mà không lo bị trùng lặp state.
- **Flask Blueprints:** Cho phép phân chia ứng dụng thành các module độc lập (`auth`, `posts`, `users`), mỗi module tự quản lý routes, templates, static files và error handlers riêng.

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Tổ chức Cấu trúc Folder Chuẩn Enterprise:**
   ```text
   flask_project/
   ├── app/
   │   ├── __init__.py        # Factory create_app()
   │   ├── extensions.py      # db instance
   │   ├── models.py          # SQLAlchemy models
   │   └── posts/
   │       ├── __init__.py
   │       └── routes.py      # Blueprint routes
   ├── config.py
   └── run.py
   ```
2. **Code chi tiết:**
   - **`app/extensions.py`:**
     ```python
     from flask_sqlalchemy import SQLAlchemy
     db = SQLAlchemy()
     ```
   - **`app/posts/routes.py`:**
     ```python
     from flask import Blueprint, jsonify, request
     from app.models import Post
     from app.extensions import db

     posts_bp = Blueprint('posts', __name__, url_prefix='/api/posts')

     @posts_bp.route('/', methods=['GET'])
     def list_posts():
         posts = Post.query.all()
         return jsonify([p.to_dict() for p in posts])
     ```
   - **`app/__init__.py`:**
     ```python
     from flask import Flask
     from app.extensions import db
     from app.posts.routes import posts_bp

     def create_app():
         app = Flask(__name__)
         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
         db.init_app(app)
         app.register_blueprint(posts_bp)
         return app
     ```

---

### 4. FL-04 — Dockerization & Container Execution
#### 🔬 Giải thích chuyên sâu:
- **WSGI Server trong Production:** Server mặc định của Flask (`app.run()`) chỉ dành cho Development (đơn luồng, không tối ưu I/O). Trong Production bắt buộc phải đứng sau một WSGI HTTP Server như **Gunicorn** hoặc **uWSGI**.
- **Multi-stage Docker Build & Layer Caching:** Tối ưu kích thước Docker Image và thời gian build bằng cách tận dụng Layer Cache của Docker (copy `requirements.txt` trước khi copy mã nguồn).

#### 🛠️ Hướng dẫn thực hành từng bước:
1. **Tạo `requirements.txt` & `Dockerfile`:**
   ```dockerfile
   # Sử dụng Python Slim nhẹ
   FROM python:3.11-slim

   # Khai báo thư mục làm việc
   WORKDIR /app

   # Tận dụng Docker Layer Caching cho dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt gunicorn

   # Copy toàn bộ mã nguồn
   COPY . .

   # Mở port container
   EXPOSE 5000

   # Chạy bằng Gunicorn trong Production (4 workers)
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
   ```
2. **Build & Execute Container:**
   ```bash
   # Build Image
   docker build -t my-flask-app:v1 .

   # Run Container đính kèm Port forwarding 5000:5000
   docker run -d -p 5000:5000 --name flask_running my-flask-app:v1
   ```
3. **Verify API bằng cURL & Logs:**
   ```bash
   curl http://localhost:5000/api/posts/
   docker logs flask_running
   ```

---

## 🎯 Bài Tập Nâng Cao
1. **Flask-Migrate integration:** Tích hợp `Flask-Migrate` (wraps Alembic) để quản lý migration schema database: `flask db init`, `flask db migrate`, `flask db upgrade`.
2. **Bảng so sánh 3 Framework:** So sánh Django vs Flask vs FastAPI theo 4 tiêu chí (Architecture & Flexibility, Learning Curve, Performance & I/O, Production Use-cases).

