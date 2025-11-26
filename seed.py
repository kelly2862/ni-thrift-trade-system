from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(
        name="Admin",
        email="admin@gmail.com",
        role="admin",
        status="active"
    )
    admin.set_password("admin123")

    user1 = User(
        name="Kelly",
        email="kelly@gmail.com",
        role="user",
        status="active"
    )
    user1.set_password("user123")

    db.session.add(admin)
    db.session.add(user1)
    db.session.commit()

    print("Database created, admin user added.")
