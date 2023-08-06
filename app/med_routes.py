from flask_restx import Resource, Namespace
from .models import Child, Medication
from .extensions import db, api
from .response_models import medication_model, add_medication_model

# endpoints for medication HTTP requests

ns_med = Namespace('medication_api')

@ns_med.route('/medications')
class MedicationList(Resource):
    @ns_med.marshal_list_with(medication_model)
    @api.doc(params={'Get': 'Look up all medications in the database'})
    def get(self):
        return Medication.query.all()
    