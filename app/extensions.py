from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

# instantiate db and api
api = Api(version='1.0', title='Tiny Tot MedTracker', description='Custom API for tracking child medications')
db = SQLAlchemy()