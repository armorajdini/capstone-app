import os

class Config:
    APP_TITLE = "3LandSpiel Spielliniengenerator MVP"
    VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    # Guardrail Settings
    MIN_THEMA_LENGTH = 5
    MIN_OUTPUT_LENGTH = 50
    
    BLACKLIST_TOPICS = [
        "waffen", "gewalt", "drogen", "porno", "extremismus", 
        "hass", "mobbing", "suizid", "selbstverletzung"
    ]
    
    ALLOWED_ZIELGRUPPEN = [
        "primarschule", "sekundarschule", "gymnasium", 
        "erwachsene", "familien", "jugendliche"
    ]

settings = Config()
