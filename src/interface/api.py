from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.application.use_cases import GenerateSpiellinie
from src.application.services import GuardrailService
from src.infrastructure.mock_llm import MockLLMGenerator

app = FastAPI(title="3LandSpiel Spielliniengenerator")

class GenerateRequest(BaseModel):
    zielgruppe: str
    thema: str

@app.post("/generate")
def generate_spiellinie(request: GenerateRequest):
    # Dependency Injection (Manuell für MVP/Einfachheit)
    generator = MockLLMGenerator()
    guardrail = GuardrailService()
    use_case = GenerateSpiellinie(generator=generator, guardrail=guardrail)
    
    try:
        spiellinie = use_case.execute(request.zielgruppe, request.thema)
        return {
            "id": str(spiellinie.id),
            "zielgruppe": {"name": spiellinie.zielgruppe.name},
            "thema": {"titel": spiellinie.thema.titel},
            "inhalt": spiellinie.inhalt
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
