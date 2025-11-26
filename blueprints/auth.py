from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from models import User
from extensions import db
from flask_login import login_required

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        pw = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(pw):
            login_user(user)
            return redirect(url_for("admin_users.list_users"))

        flash("Invalid email or password!", "danger")

    return render_template("auth_login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
