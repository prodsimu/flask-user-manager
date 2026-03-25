import os

from flask import Flask

from app.database.seeds import seed_admin

from .database.database import db
from .models import User


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "supersecretkey123")

    db.init_app(app)

    from .models import User
    from .routes import user_bp

    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()

    with app.app_context():
        db.create_all()
        created = seed_admin()

        if created:
            print("Admin created: username=admin | password=admin123")

    return app
