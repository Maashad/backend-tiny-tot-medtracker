from flask_restx import Resource, Namespace
from .models import Child, Medication
from .extensions import db, api
from .response_models import child_model, add_child_model

# set up endpoints for HTTP requests

ns = Namespace("api")

@ns.route("/children")
class ChildrenList(Resource):
    @ns.marshal_list_with(child_model)
    @api.doc(params={'Get': 'Look up all children in the database'})
    def get(self):
        return Child.query.all()
    
    @ns.expect(add_child_model)
    @ns.marshal_with(child_model)
    @api.doc(params={'Name': 'Add one child to the database'})
    def post(self):
        child = Child(name=ns.payload['name'])

        db.session.add(child)
        db.session.commit()

        return child, 201

@ns.route('/children/<int:id>', endpoint='children')
@api.doc(responses={404: "child not found"})
@api.doc(responses={200: "success"})
class Children(Resource):
    @ns.marshal_with(child_model)
    @api.doc(params={'id': 'Record id to display'})
    def get(self, id):
        child = Child.query.get(id)

        return child
    
    @ns.expect(add_child_model)
    @ns.marshal_with(child_model)
    @api.doc(params={'id': 'Record id to update'})
    def put(self, id):
        child = Child.query.get(id)
        child.name = ns.payload['name']

        db.session.add(child)
        db.session.commit()

        return child, 200
    
    @api.doc(params={'id': 'Record id to delete'})
    def delete(self, id):
        child = Child.query.get(id)

        db.session.delete(child)
        db.session.commit()

        return {}, 204