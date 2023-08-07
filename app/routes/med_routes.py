from flask_restx import Resource, Namespace
from ..models.medication_model import Medication
from ..extensions import db, api
from ..models.response_models import medication_model, add_medication_model

# endpoints for medication HTTP requests

ns_med = Namespace('medication_api')

@ns_med.route('/medications')
class MedicationList(Resource):
    @ns_med.marshal_list_with(medication_model)
    @api.doc(params={'Get': 'Look up all medications in the database'})
    def get(self):
        return Medication.query.all()
    
    @ns_med.expect(add_medication_model)
    @ns_med.marshal_with(medication_model)
    def post(self):
        medication = Medication(
            name=ns_med.payload['name'],
            dose=ns_med.payload['dose'],
            frequency=ns_med.payload['frequency']
        )

        db.session.add(medication)
        db.session.commit()

        return medication, 201

@ns_med.route('/medications/<int:id>', endpoint='medications')
class Medications(Resource):
    @ns_med.marshal_with(medication_model)
    def get(self, id):
        medication = Medication.query.get(id)

        return medication, 200

    @api.doc(params={'id': 'Record id to delete'})
    def delete(self, id):
        medication = Medication.query.get(id)

        db.session.delete(medication)
        db.session.commit()

        return {}, 204