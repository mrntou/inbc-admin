# Database for INBC-AMDIN users
from IA import app, db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    image = db.Column(db.String(), default="user_default.png")
    is_admin = db.Column(db.Boolean, default=True)
    password_hash = db.Column(db.String())

    def __init__(self, username):
        self.username = username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User> {self.username}"
