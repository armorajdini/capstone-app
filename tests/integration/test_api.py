import pytest
from fastapi.testclient import TestClient
from src.interface.api import app

client = TestClient(app)

def test_generate_spiellinie_endpoint_success():
    response = client.post(
        "/generate",
        json={"zielgruppe": "Primarschule", "thema": "Rhein-Abenteuer"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "inhalt" in data
    assert "zielgruppe" in data
    assert data["zielgruppe"]["name"] == "Primarschule"

def test_generate_spiellinie_endpoint_invalid_input():
    # 'waffen' ist auf der Blacklist im GuardrailService
    response = client.post(
        "/generate",
        json={"zielgruppe": "Primarschule", "thema": "Gefährliche Waffen"}
    )
    
    assert response.status_code == 400
    assert "validation failed" in response.json()["detail"].lower()
