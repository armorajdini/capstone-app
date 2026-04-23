import httpx
import pytest

# Basis-URL für die laufende App (z.B. im Docker-Container)
BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_e2e_generate_spiellinie():
    payload = {
        "zielgruppe": "Sekundarschule",
        "thema": "Historie von Basel"
    }
    
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/generate", json=payload)
        
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "inhalt" in data
    assert data["zielgruppe"]["name"] == "Sekundarschule"

@pytest.mark.asyncio
async def test_e2e_guardrail_rejection():
    payload = {
        "zielgruppe": "Primarschule",
        "thema": "Gewalttätige Auseinandersetzungen" # Enthält 'gewalt' -> Blacklist
    }
    
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/generate", json=payload)
        
    assert response.status_code == 400
    assert "validation failed" in response.json()["detail"].lower()
