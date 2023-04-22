from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.py import app
import pytest

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
