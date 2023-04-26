import json

def test_create_user(client):
    data = {"user":"schemas.UserCreate", "email":"user.email","response_model":"schemas.UserSchema"}
    response = client.post("/", json.dumps(data))
    assert response.status_code == 400
    assert response.json()["email"] == "user.email"
