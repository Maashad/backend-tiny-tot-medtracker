from flask import Flask
from .extensions import api, db
from .routes.child_routes import ns_child
from .routes.med_routes import ns_med

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.tinytot"

    from app.models.medication_model import Medication
    from app.models.child_model import Child

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns_child)
    api.add_namespace(ns_med)

    return app
