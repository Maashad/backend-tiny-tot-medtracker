from flask import Flask
from flask_migrate import Migrate
from .extensions import api, db
from .routes.child_routes import ns_child
from .routes.med_routes import ns_med

def create_app():
    app = Flask(__name__)

    migrate = Migrate(app, db)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/tinytot'

    from app.models.medication_model import Medication
    from app.models.child_model import Child

    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_namespace(ns_child)
    api.add_namespace(ns_med)

    return app
