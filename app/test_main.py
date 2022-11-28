
from fastapi.testclient import TestClient
from .main import application
import json

client = TestClient(application)

def test_getUserIds_empty():
    response = client.get("/users")
    assert json.loads(response.content) == []

def test_add():
    body = {"name":"andreas","age":26,"company":"Devoteam"}
    response =client.post("/users",json=body)
    assert response.status_code == 201

def test_getUserIds_notEmpty():
    response = client.get("/users")
    assert json.loads(response.content) == ['andreas']

def test_schema_validation():
    body = {"name":"andreas","age":"twentysix","company":"Devoteam"}
    response =client.post("/users/",json=body)
    assert response.status_code == 422