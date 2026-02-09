import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_docs_endpoint():
    response = client.get("/docs")
    # Swagger UI should be available, status code 200
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text  # Basic check that HTML page is returned
