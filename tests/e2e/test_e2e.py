import httpx
import pytest

# Basis-URL für die laufende App
BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_e2e_generate_and_check_library():
    target_thema = "Die Rheinschifffahrt"
    payload = {
        "zielgruppe": "Sekundarschule",
        "thema": target_thema,
        "user_name": "Frau Lehrerin",
        "lernziele": ["Geschichte verstehen", "Handel lernen"]
    }
    
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # 1. Generieren
        gen_response = await client.post("/generate", json=payload)
        assert gen_response.status_code == 200
        
        # 2. In der Library suchen
        lib_response = await client.get("/library")
        assert lib_response.status_code == 200
        
        library = lib_response.json()
        themen = [item["thema"] for item in library]
        assert target_thema in themen

@pytest.mark.asyncio
async def test_e2e_guardrail_rejection():
    payload = {
        "zielgruppe": "Primarschule",
        "thema": "Drogenkonsum am Rheinufer", # Blacklist: 'drogen'
        "user_name": "Test User"
    }
    
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/generate", json=payload)
        
    assert response.status_code == 400
    assert "validation failed" in response.json()["detail"].lower()

@pytest.mark.asyncio
async def test_e2e_frontend_served():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "3LandSpiel Spielliniengenerator" in response.text
