from flask import Flask
from blueprints.auth import bp as auth_bp
from blueprints.admin_users import bp as admin_users_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_users_bp)

app = Flask(__name__)

@app.route("/")
def home():
    return "Uni Thrift System Running!"

if __name__ == "__main__":
    app.run(debug=True)
