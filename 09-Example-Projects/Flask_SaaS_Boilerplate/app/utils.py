from functools import wraps
from flask import request, jsonify, g
from app.models import User

def token_required(f):
    """Simple token decorator (Mocking JWT for logic example)"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        # In real world: Decode JWT here
        user = User.query.filter_by(username='admin').first() # Mocking
        g.current_user = user
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    """Ensures user has admin role"""
    @wraps(f)
    def decorated(*args, **kwargs):
        # Logic check: isAdmin?
        if not g.current_user or g.current_user.username != 'admin':
            return jsonify({'message': 'Admin permission required!'}), 403
        return f(*args, **kwargs)
    return decorated

# Senior Audit Log Logic
class AuditLogger:
    @staticmethod
    def log_action(user_id, action, target_type):
        """Logic to save activity history"""
        # In real life: Save to an 'ActivityLog' model
        print(f"AUDIT LOG: User {user_id} performed '{action}' on {target_type}")
