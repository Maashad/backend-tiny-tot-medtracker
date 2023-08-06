# Models to represent the structure of a JSON serializable HTTP response

from flask_restx import fields
from .extensions import api

child_model = api.model("Child", {
    "id": fields.Integer,
    "name": fields.String
})

add_child_model = api.model('AddChild', {
    "name": fields.String
})