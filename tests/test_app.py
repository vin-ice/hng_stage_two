#!/usr/bin/python3
import pytest
import app

@pytest.fixture()
def client():
    """create a test client for the application."""
    with app.app.test_client() as client:
        user_id = None
        yield client

def test_add_user(client):
    """test adding a user through the /api POST endpoint."""
    data = {
        'name': 'John Doe',
        'value': 'Missing Bio'
    }
    response = client.post('/api', json=data)
    assert response.status_code == 201
    response_data = response.get_json()
    assert isinstance(response_data, dict)
    assert response_data['name'] == 'John Doe'
    assert response_data['value'] == 'Missing Bio'
    assert 'user_id' in response_data.keys()


def test_get_user(client):
    """test adding a user through the /api POST endpoint."""
    data = {
        'name': 'John Doe',
        'value': 'Missing Bio'
    }
    res = client.post('/api', json={"name": "Jane", "value": "The gaijin"})
    assert res.status_code == 201
    res_data = res.get_json()
    assert isinstance(res_data, dict)
    response = client.get(f'/api/{res_data["user_id"]}', json=data)
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['name'] == 'Jane'
    assert response_data['value'] == 'The gaijin'
    assert 'user_id' in response_data.keys()

def test_update_user(client):
    """test update"""
    """test adding a user through the /api POST endpoint."""
    data = {'name': 'John Doe','value': 'Missing Bio'}
    data_2 = {"name": "Jane Doe", "value": "Missing Bio"}
    response = client.post('/api', json=data)
    assert response.status_code == 201
    response_data = response.get_json()

    update_res = client.put(f'/api/{response_data["user_id"]}', json=data_2)
    assert update_res.status_code == 200
    update_res_data = update_res.get_json()
    assert update_res_data['name'] == data_2['name']


def test_update_user(client):
    """test delete"""
    """test deleteing a user"""
    data = {'name': 'John Doe', 'value': 'Missing Bio'}
    response = client.post('/api', json=data)
    assert response.status_code == 201
    response_data = response.get_json()

    res = client.delete(f'/api/{response_data["user_id"]}')
    assert res.status_code == 200
