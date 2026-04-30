import pytest
from fastapi.testclient import TestClient
from src.interface.api import app

client = TestClient(app)

def test_generate_spiellinie_endpoint_success():
    response = client.post(
        "/generate",
        json={"zielgruppe": "Primarschule", "thema": "Rhein-Abenteuer", "user_name": "Test Lehrer"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "inhalt" in data
    assert "stationen" in data
    assert len(data["stationen"]) == 1 # Default station
    assert data["ersteller"]["name"] == "Test Lehrer"

def test_generate_spiellinie_endpoint_invalid_input():
    # 'waffen' ist auf der Blacklist im GuardrailService
    response = client.post(
        "/generate",
        json={"zielgruppe": "Primarschule", "thema": "Gefährliche Waffen", "user_name": "Test Lehrer"}
    )
    
    assert response.status_code == 400
    assert "validation failed" in response.json()["detail"].lower()

def test_library_endpoint():
    target_thema = "Basel Geschichte"
    # Zuerst eine generieren (mit user_name!)
    res = client.post(
        "/generate",
        json={"zielgruppe": "Gymnasium", "thema": target_thema, "user_name": "Test Lehrer"}
    )
    assert res.status_code == 200
    
    response = client.get("/library")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    # Prüfen ob unser Thema in der Liste ist
    themen = [item["thema"] for item in data]
    assert target_thema in themen

def test_static_files_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "3LandSpiel Spielliniengenerator" in response.text
