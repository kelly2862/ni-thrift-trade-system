from flask import Blueprint, render_template, redirect, url_for
from extensions import db
from models import User

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Show all users
@admin_bp.route("/users")
def manage_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)

# Suspend user
@admin_bp.route("/suspend/<int:user_id>")
def suspend_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.status = "suspended"
        db.session.commit()
    return redirect(url_for("admin.manage_users"))

# Activate user
@admin_bp.route("/activate/<int:user_id>")
def activate_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.status = "active"
        db.session.commit()
    return redirect(url_for("admin.manage_users"))

# Delete user
@admin_bp.route("/delete/<int:user_id>")
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("admin.manage_users"))
