import json

def test_get_hospitals(client):
    data = {"response_model": "list[schemas.HospitalCreate]", "skip":"int = 0", "limit": "int = 100"}
    response= client.get("/", json.dumps(data))
    assert response.status_code == 200
    if hospitals is None:
       assert response.status_code == 404
       assert response.json(){"detail":"Hospital not found"}
    assert response.json()["skip"] == "skip"
    assert response.json()["limit"] == "limit"
