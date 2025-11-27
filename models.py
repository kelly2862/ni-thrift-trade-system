from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="user")   # admin / user
    status = db.Column(db.String(20), default="active")  # active / suspended

    # Set hashed password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check hashed password
    def check_password(self, password):
        return check_password_hash(self.password, password)

