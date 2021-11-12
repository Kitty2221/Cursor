import pytest
from app import app, db


@pytest.fixture
def client():
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@db:3306/flask'
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client


def test_get_plant(client):
    res = client.get("/api/v1/plants")
    assert res.status_code == 200
    assert ('Lviv', str(res.data))


def test_api_can_get_plant_by_id(client):
    res = client.get('/api/v1/plants/1')
    assert (res.status_code, 200)
    assert ('Ooo', str(res.data))


def test_plant_deletion(client):
    res = client.delete('/api/v1/plants/31')
    assert (res.status_code, 204)
    res = client.get('/api/v1/plants/31')
    assert (res.status_code, 404)


def test_get_employee(client):
    res = client.get("/api/v1/employees")
    assert res.status_code == 200
    assert ('Kiee@gmail.com', str(res.data))


def test_api_can_get_employee_by_id(client):
    res = client.get('/api/v1/employees/5')
    assert (res.status_code, 200)
    assert ('Kitty', str(res.data))


def test_employee_deletion(client):
    res = client.delete('/api/v1/employees/10')
    assert (res.status_code, 204)
    res = client.get('/api/v1/employees/10')
    assert (res.status_code, 404)


def test_get_salons(client):
    res = client.get("/api/v1/salons")
    assert res.status_code == 200
    assert ('str Molodi 112/1', str(res.data))


def test_api_can_get_salons_by_id(client):
    res = client.get('/api/v1/salons/4')
    assert (res.status_code, 200)
    assert ('Silpo', str(res.data))


def test_salons_deletion(client):
    res = client.delete('/api/v1/salons/7')
    assert (res.status_code, 204)
    res = client.get('/api/v1/salons/7')
    assert (res.status_code, 404)


def test_get_models(client):
    res = client.get("/api/v1/salons")
    assert res.status_code == 200
    assert ('plants', str(res.data))

