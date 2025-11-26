from app import create_app
from extensions import db
from models import User

# Initialize the app
app = create_app()

# Use the app's context for database operations
with app.app_context():
    db.drop_all()  # Clear all tables
    db.create_all()  # Create all tables (like 'users')

    # Admin user
    admin = User(
        name="Admin",
        email="admin@gmail.com",
        role="admin",
        status="active"
    )
    admin.set_password("admin123")

    # Regular user
    user1 = User(
        name="Kelly",
        email="kelly@gmail.com",
        role="user",
        status="active"
    )
    user1.set_password("user123")

    # Add users to the session and commit
    db.session.add(admin)
    db.session.add(user1)
    db.session.commit()  # Commit changes

    print("Database created, admin user added.")
