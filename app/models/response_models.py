# Models to represent the structure of a JSON serializable HTTP response

from flask_restx import fields
from ..extensions import api

medication_model = api.model('Medications', {
    'id': fields.Integer,
    'name': fields.String,
    'dose': fields.String,
    'frequency': fields.Integer,
    'child_id': fields.Integer
})

child_model = api.model('Child', {
    'id': fields.Integer,
    'name': fields.String,
    'medications': fields.List(fields.Nested(medication_model))
})

add_child_model = api.model('AddChild', {
    'name': fields.String
})

add_medication_model = api.model('AddMedication', {
    'name': fields.String,
    'dose': fields.String,
    'frequency': fields.Integer
})
