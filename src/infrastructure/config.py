import os
from pathlib import Path

# Absoluter Pfad zum Projekt-Root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    # API Einstellungen
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "3LandSpiel - AI Spielliniengenerator")
    API_V1_STR: str = "/api/v1"
    
    # Datenbank Einstellungen
    _db_url = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/3landspiel_v2.db")
    
    # SQLAlchemy braucht 'postgresql://' statt 'postgres://' (falls Render das so liefert)
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    
    DATABASE_URL: str = _db_url

    # Business Logic / Guardrail Einstellungen
    BLACKLIST_TOPICS: list = ["drogen", "waffen", "gewalt", "politik", "extremismus"]
    ALLOWED_ZIELGRUPPEN: list = ["primarschule", "sekundarschule", "gymnasium", "erwachsene"]
    MIN_THEMA_LENGTH: int = 3
    MIN_OUTPUT_LENGTH: int = 10

settings = Settings()
