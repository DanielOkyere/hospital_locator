import json
from tests.test_routes import configtest.py
from api.models.hospital import schemas, crud

def test_get_hospitals(client):
    data = {"response_model": "list[schemas.HospitalCreate]", "skip":"int = 0", "limit": "int = 100"}
    response= client.get("/", json.dumps(data))
    assert response.status_code == 200
    if hospitals is None:
       assert response.status_code == 404
       assert response.json(){"detail":"Hospital not found"}
    assert response.json()["skip"] == "skip"
    assert response.json()["limit"] == "limit"

def test_get_hospitals_by_name(client):
    data = {"response_model":"list[schemas.HospitalCreate]", "hospital_name": "str", "skip":"int = 0", "limit":"int = 20"}
    response = client.get("/{hospital_name}", json.dumps(data))
    assert response.status_code == 200
    if hospitals is None:
       assert response.status_code == 404
       assert response.json(){"detail":"Hospital not found"}
    assert response.json()["hospital_name"] == "hospital_name"
    assert response.json()["skip"] == "skip"
    assert response.json()["limit"] == "limit"

def test_get_hospitals_by_id(client):
    data = {"response_model":"schemas.HospitalCreate", "hospital_id":"int"}
    response = client.get("/id/{hospital_id}", json.dumps(data)
    assert response.status_code == 200
    if hospitals is None:
       assert response.status_code == 404
       assert response.json(){"detail":"Hospital not found"}
    assert response.json()["hospital_id"] == "hospital_id"
