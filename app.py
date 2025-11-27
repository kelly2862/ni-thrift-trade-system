from flask import Flask
from config import Config
from extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints INSIDE the create_app function
    from blueprints.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from blueprints.admin_users import admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app


# Only used when running `python app.py`
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
