import os
import sys

from flask import Flask
from app.config import Config
from app.models import db
from app.routes import register_routes


def create_app():

    if getattr(sys, "frozen", False):
        # Running as PyInstaller EXE
        base_path = os.path.join(sys._MEIPASS, "app")
    else:
        # Running normally
        base_path = os.path.dirname(os.path.abspath(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_path, "templates"),
        static_folder=os.path.join(base_path, "static")
    )

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app