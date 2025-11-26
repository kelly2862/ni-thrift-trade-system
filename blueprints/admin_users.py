from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import User

bp = Blueprint("admin_users", __name__, url_prefix="/admin/users")

# Admin-only decorator
def admin_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            return "Forbidden: Admins only", 403
        return func(*args, **kwargs)
    return wrapper


@bp.route("/")
@login_required
@admin_required
def list_users():
    q = request.args.get("q", "")
    
    if q:
        users = User.query.filter(
            (User.name.ilike(f"%{q}%")) | (User.email.ilike(f"%{q}%"))
        ).all()
    else:
        users = User.query.all()

    return render_template("admin_users.html", users=users, q=q)


@bp.post("/<int:user_id>/status")
@login_required
@admin_required
def change_status(user_id):
    user = User.query.get_or_404(user_id)
    new_status = request.form["status"]

    if new_status not in ["active", "suspended", "deleted"]:
        flash("Invalid status!", "danger")
        return redirect(url_for("admin_users.list_users"))
    
    user.status = new_status
    db.session.commit()

    flash(f"User {user.email} status updated to: {new_status}", "success")
    return redirect(url_for("admin_users.list_users"))
