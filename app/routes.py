from flask_restx import Resource, Namespace
from .models import Child, Medication
from .extensions import db, api
from .response_models import child_model, add_child_model

# set up endpoints for HTTP requests

ns = Namespace("api")

@ns.route("/children")
@api.doc(responses={404: "children not found, please add a child"})
@api.doc(responses={200: "success"})
@api.doc(params={'all': 'Look up all children in the database'})
class ChildrenList(Resource):
    @ns.marshal_list_with(child_model)
    def get(self):
        return Child.query.all()
    
    @ns.expect(add_child_model)
    @ns.marshal_with(child_model)
    def post(self):
        child = Child(name=ns.payload['name'])

        db.session.add(child)
        db.session.commit()

        return child, 201
