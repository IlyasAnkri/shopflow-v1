from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
BASE_URL = "/api/orders"

def test_create_order():
    response = client.post(BASE_URL, json={"product": "Serveur", "quantity": 1, "price": 1200.0})
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_orders():
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_invalid_order():
    response = client.post(BASE_URL, json={"product": "Câble", "quantity": "dix", "price": 15.0})
    assert response.status_code == 422
