from backend.server import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_user_create_success():
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "password": "Password123"
    }

    response = client.post("/v1/auth/user/create", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_user_create_pw_fail():
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "password": "badpassword"
    }

    response = client.post("/v1/auth/user/create", json=payload)
    assert response.status_code == 422