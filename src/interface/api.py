from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
import os

from src.application.use_cases import GenerateSpiellinie, GetSpiellinieLibrary, GetSpiellinieDetail
from src.application.services import GuardrailService
from src.infrastructure.mock_llm import MockLLMGenerator
from src.infrastructure.llm import LiteLLMGenerator
from src.infrastructure.database import SessionLocal, engine, Base, get_db
from src.infrastructure.repositories import SqlAlchemySpiellinieRepository
from src.infrastructure.config import settings

# Datenbank Tabellen erstellen
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

class StationRequest(BaseModel):
    name: str
    ort: str
    aufgabe: str

class GenerateRequest(BaseModel):
    zielgruppe: str
    thema: str
    user_name: str
    schule: Optional[str] = "3Land-Schule"
    lernziele: List[str] = []
    stationen_plan: Optional[List[StationRequest]] = None

@app.post("/generate")
def generate_spiellinie(request: GenerateRequest, db: Session = Depends(get_db)):
    if settings.USE_MOCK_LLM:
        generator = MockLLMGenerator()
    else:
        generator = LiteLLMGenerator()
        
    guardrail = GuardrailService()
    repository = SqlAlchemySpiellinieRepository(db)
    use_case = GenerateSpiellinie(generator=generator, guardrail=guardrail, repository=repository)
    
    try:
        spiellinie = use_case.execute(
            zielgruppe_name=request.zielgruppe,
            thema_titel=request.thema,
            user_name=request.user_name,
            schule=request.schule,
            lernziele_list=request.lernziele,
            stationen_plan=request.stationen_plan
        )
        
        return {
            "id": str(spiellinie.id),
            "ersteller": {"name": spiellinie.user.name, "schule": spiellinie.user.schule},
            "zielgruppe": {"name": spiellinie.zielgruppe.name},
            "thema": {"titel": spiellinie.thema.titel},
            "inhalt": spiellinie.inhalt,
            "stationen": [
                {
                    "name": s.name, 
                    "ort": s.ort, 
                    "aufgabe": s.aufgabe.beschreibung if s.aufgabe else ""
                } for s in spiellinie.stationen
            ],
            "lernziele": [lz.beschreibung for lz in spiellinie.lernziele]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/library")
def get_library(zielgruppe: Optional[str] = None, db: Session = Depends(get_db)):
    repository = SqlAlchemySpiellinieRepository(db)
    use_case = GetSpiellinieLibrary(repository=repository)
    
    library = use_case.execute(zielgruppe_filter=zielgruppe)
    return [
        {
            "id": str(sl.id),
            "ersteller": sl.user.name,
            "thema": sl.thema.titel,
            "zielgruppe": sl.zielgruppe.name,
            "anzahl_stationen": len(sl.stationen),
            "lernziele": [lz.beschreibung for lz in sl.lernziele]
        } for sl in library
    ]

@app.get("/library/{id}")
def get_spiellinie_detail(id: str, db: Session = Depends(get_db)):
    repository = SqlAlchemySpiellinieRepository(db)
    use_case = GetSpiellinieDetail(repository=repository)
    
    sl = use_case.execute(spiellinie_id=id)
    if not sl:
        raise HTTPException(status_code=404, detail="Spiellinie not found")
        
    return {
        "id": str(sl.id),
        "ersteller": {"name": sl.user.name, "schule": sl.user.schule},
        "zielgruppe": {"name": sl.zielgruppe.name},
        "thema": {"titel": sl.thema.titel},
        "inhalt": sl.inhalt,
        "stationen": [
            {
                "name": s.name, 
                "ort": s.ort, 
                "aufgabe": s.aufgabe.beschreibung if s.aufgabe else ""
            } for s in sl.stationen
        ],
        "lernziele": [lz.beschreibung for lz in sl.lernziele]
    }

# Statische Dateien (Frontend) mounten
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_path, html=True), name="static")
