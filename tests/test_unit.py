import json
import pytest
from flask import Flask
from myapp import app as application


@pytest.fixture()
def app():
    app = application.application
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


def test_getUserIds_empty(client):
    response = client.get("/")
    assert json.loads(response.data) == []

def test_add(client):
    body = {"name":"andreas","age":26,"company":"Devoteam"}
    response =client.post("/",json=body)
    assert response.status_code == 201
    
def test_getUserIds_notEmpty(client):
    response = client.get("/")
    assert json.loads(response.data) == ['andreas']

def test_schema_validation(client):
    body = {"name":"andreas","age":"twentysix","company":"Devoteam"}
    response =client.post("/",json=body)
    assert response.status_code == 400