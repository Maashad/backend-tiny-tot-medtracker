from flask_restx import Resource, Namespace
from .models import Child, Medication
from .extensions import db, api
from .response_models import child_model, add_child_model

# endpoints for child HTTP requests

ns_child = Namespace('child_api')

@ns_child.route('/children')
class ChildrenList(Resource):
    @ns_child.marshal_list_with(child_model)
    @api.doc(params={'Get': 'Look up all children in the database'})
    def get(self):
        return Child.query.all()
    
    @ns_child.expect(add_child_model)
    @ns_child.marshal_with(child_model)
    @api.doc(params={'Name': 'Add one child to the database'})
    def post(self):
        child = Child(name=ns_child.payload['name'])

        db.session.add(child)
        db.session.commit()

        return child, 201

@ns_child.route('/children/<int:id>', endpoint='children')
@api.doc(respons_childes={404: "child not found"})
@api.doc(respons_childes={200: "success"})
class Children(Resource):
    @ns_child.marshal_with(child_model)
    @api.doc(params={'id': 'Record id to display'})
    def get(self, id):
        child = Child.query.get(id)

        return child
    
    @ns_child.expect(add_child_model)
    @ns_child.marshal_with(child_model)
    @api.doc(params={'id': 'Record id to update'})
    def put(self, id):
        child = Child.query.get(id)
        child.name = ns_child.payload['name']

        db.session.add(child)
        db.session.commit()

        return child, 200
    
    @api.doc(params={'id': 'Record id to delete'})
    def delete(self, id):
        child = Child.query.get(id)

        db.session.delete(child)
        db.session.commit()

        return {}, 204