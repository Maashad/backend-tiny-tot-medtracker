from flask import Flask
from .extensions import api, db
from .routes import ns

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.tinytot"

    from app.models import Child, Medication

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app
