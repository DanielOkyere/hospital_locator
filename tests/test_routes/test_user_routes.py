import json
from tests.test_routes import configtest.py
from api.models.user import schemas, crud

def test_create_user(client):
    data = {"user":"schemas.UserCreate", "email":"user.email","response_model":"schemas.UserSchema"}
    response = client.post("/", json.dumps(data))
    assert response.status_code == 400
    assert response.json()["email"] == "user.email"
    assert response.json() == {"detail": "Email already exist"}

def test_read_user(client):
    data = {"user_id": "int", "response_model": "schemas.UserSchema"}
    response = client.get("/{user_id}", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["user_id"] == "user_id"
    if db_user is None:
       assert response.status_code == 404
       assert response.json() == {"detail": "User not found"}

def test_read_users(client):
    data = {"response_model":"list[schemas.UserSchema]", "skip":"int = 0", "limit":"int = 100"}
    response = client.get("/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["skip"] == "skip"
    assert response.json()["limit"] == "limit"

def test_delete_user(client):
    data = {"user_id": "int"}
    response = client.delete("/{user_id}", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["id"] == "user_id"
