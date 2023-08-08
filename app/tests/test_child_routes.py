import pytest
from ..routes import child_routes
from ..models.response_models import child_model

def test_get_all_children_with_no_records():
    response = client.get('/children')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []
