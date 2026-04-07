from flask import Blueprint, jsonify, request
from app.services import UserService, SubscriptionService
from app.models import User

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['POST'])
def register():
    data = request.get_json() or {}
    user, error = UserService.create_user(
        data.get('username'), 
        data.get('email'), 
        data.get('password')
    )
    
    if error:
        return jsonify({"error": error}), 400
    
    # Automatically start trial
    SubscriptionService.start_trial(user)
    
    return jsonify({
        "message": "User registered and 14-day trial started!",
        "user_id": user.id
    }), 201
