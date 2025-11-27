from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import User
from extensions import db, login_manager

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

# Required by Flask-Login to load user from session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------------------
# LOGIN PAGE
# ------------------------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Email does not exist", "error")
            return redirect(url_for("auth.login"))

        if not user.check_password(password):
            flash("Incorrect password", "error")
            return redirect(url_for("auth.login"))

        if user.status != "active":
            flash("Your account is not active", "error")
            return redirect(url_for("auth.login"))

        login_user(user)
        flash("Logged in successfully!", "success")

        # Redirect admin / user separately
        if user.role == "admin":
            return redirect(url_for("admin.manage_users"))
        else:
            return redirect(url_for("auth.dashboard"))

    return render_template("auth_login.html")



# ------------------------------
# LOGOUT
# ------------------------------
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out!", "success")
    return redirect(url_for("auth.login"))


# ------------------------------
# OPTIONAL: USER DASHBOARD
# ------------------------------
@auth_bp.route("/dashboard")
@login_required
def dashboard():
    return "User Dashboard (you can design this later)"
