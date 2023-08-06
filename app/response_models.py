from flask_restx import fields
from .extensions import api

child_model = api.model("Child", {
    "id": fields.Integer,
    "name": fields.String
})