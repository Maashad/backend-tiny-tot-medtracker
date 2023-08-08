from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from .extensions import api, db
from .routes.child_routes import ns_child
from .routes.med_routes import ns_med

load_dotenv

def create_app(test_config=None):
    app = Flask(__name__)

    migrate = Migrate(app, db)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    from app.models.medication_model import Medication
    from app.models.child_model import Child

    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_namespace(ns_child)
    api.add_namespace(ns_med)

    return app
