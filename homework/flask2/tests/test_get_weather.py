from tests.conftest import client
from config import Config


def test_search_weather(client):
    response = client.get("/get-your-weather")
    assert response.status_code == 200


def test_weather_true(client):
    response = client.get('/get-your-weather')
    assert b"Timezone" in response.data
