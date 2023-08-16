import pytest
from extensions import db
from app import create_app
from app.models.child_model import Child

# Setup a test configuration
@pytest.fixture
def app():
    app = create_app(config_name="testing")
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

def test_get_all_children_empty_db(client, init_db):
    response = client.get('/children')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_child(client, init_db):
    response = client.post('/children', json={'name': 'John'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'John'

def test_get_child_by_id(client, init_db):
    child = Child(name="Jane")
    init_db.session.add(child)
    init_db.session.commit()
    
    response = client.get(f'/children/{child.id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Jane'

def test_get_child_invalid_id(client, init_db):
    response = client.get('/children/999')
    assert response.status_code == 404

def test_update_child(client, init_db):
    child = Child(name="Jane")
    init_db.session.add(child)
    init_db.session.commit()
    
    response = client.put(f'/children/{child.id}', json={'name': 'Jane Updated'})
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Jane Updated'

def test_update_child_invalid_id(client, init_db):
    response = client.put('/children/999', json={'name': 'Jane Updated'})
    assert response.status_code == 404

def test_delete_child(client, init_db):
    child = Child(name="Jane")
    init_db.session.add(child)
    init_db.session.commit()
    
    response = client.delete(f'/children/{child.id}')
    assert response.status_code == 204
    assert Child.query.get(child.id) is None

def test_delete_child_invalid_id(client, init_db):
    response = client.delete('/children/999')
    assert response.status_code == 404
