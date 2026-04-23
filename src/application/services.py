from src.domain.interfaces import IGuardrailService
from src.domain.value_objects import Zielgruppe, Thema, Prompt
from src.infrastructure.config import settings

class GuardrailService(IGuardrailService):
    def __init__(self):
        self.blacklist_topics = settings.BLACKLIST_TOPICS
        self.allowed_zielgruppen = settings.ALLOWED_ZIELGRUPPEN
        self.min_thema_length = settings.MIN_THEMA_LENGTH
        self.min_output_length = settings.MIN_OUTPUT_LENGTH

    def validate_input(self, zielgruppe: Zielgruppe, thema: Thema) -> bool:
        if zielgruppe.name.lower() not in self.allowed_zielgruppen:
            return False
            
        text_to_check = f"{thema.titel}".lower()
        for word in self.blacklist_topics:
            if word in text_to_check:
                return False
                
        if len(thema.titel.strip()) < self.min_thema_length:
            return False
            
        return True

    def enrich_prompt(self, zielgruppe: Zielgruppe, thema: Thema) -> Prompt:
        prompt_text = (
            f"SYSTEM: Du bist ein KI-Experte für das '3LandSpiel', ein erlebnispädagogisches "
            f"Projekt im Dreiländereck (CH, DE, FR). Deine Aufgabe ist es, sichere, "
            f"didaktisch wertvolle und spannende Spiellinien zu entwerfen.\n"
            f"ZIELGRUPPE: {zielgruppe.name}\n"
            f"THEMA: {thema.titel}\n\n"
            f"ANWEISUNG: Erstelle eine Spiellinie mit 3 Phasen (Start, Aktivität, Abschluss). "
            f"Beziehe lokale Gegebenheiten des Rheins oder des 3Land-Areals ein. "
            f"Verwende eine Sprache, die für {zielgruppe.name} angemessen ist."
        )
        return Prompt(text=prompt_text)

    def verify_output(self, raw_content: str) -> bool:
        unsafe_words = ["hass", "gewalt", "töten", "mord", "blut"]
        content_lower = raw_content.lower()
        for word in unsafe_words:
            if word in content_lower:
                return False
                
        if len(raw_content.strip()) < self.min_output_length:
            return False
            
        return True
