from app.models import User, Subscription
from app import db
from datetime import datetime, timedelta

class UserService:
    @staticmethod
    def create_user(username, email, password):
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user, None

class SubscriptionService:
    @staticmethod
    def start_trial(user):
        """Start a 14-day trial for new users"""
        expires_at = datetime.utcnow() + timedelta(days=14)
        sub = Subscription(plan_name='free_trial', user_id=user.id, expires_at=expires_at)
        db.session.add(sub)
        db.session.commit()
        return sub

# Senior Tip: Using a Service Layer keeps your routes thin and your business logic testable!
