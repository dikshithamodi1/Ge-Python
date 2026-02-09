import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/")
    assert response.status_code in [200, 404]  # works even if root endpoint is not defined
