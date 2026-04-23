import re
from src.domain.interfaces import ISpiellinienGenerator
from src.domain.value_objects import Prompt

class MockLLMGenerator(ISpiellinienGenerator):
    def generate(self, prompt: Prompt) -> str:
        # Extrahiere Thema und Zielgruppe aus dem Prompt für eine "plausible" Antwort
        # (Dies simuliert ein LLM, das den Prompt liest)
        thema_match = re.search(r"THEMA: (.*)", prompt.text)
        zg_match = re.search(r"ZIELGRUPPE: (.*)", prompt.text)
        
        thema = thema_match.group(1) if thema_match else "Unbekanntes Thema"
        zielgruppe = zg_match.group(1) if zg_match else "alle Altersgruppen"
        
        return (
            f"--- Spiellinie: {thema} für {zielgruppe} ---\n\n"
            f"1. Start: Die Gruppe trifft sich an der Dreiländerbrücke. Ein geheimnisvoller Brief "
            f"aus der Zukunft warnt vor einer ökologischen Krise am Rhein.\n\n"
            f"2. Aktivität: Die Teilnehmenden müssen Wasserproben entnehmen und spielerisch "
            f"die Strömung analysieren. Dabei lernen sie die Bedeutung der Rheinschifffahrt kennen.\n\n"
            f"3. Abschluss: Gemeinsame Auswertung der Ergebnisse im 'Hafen-Camp'. Die Gruppe "
            f"erhält ein Zertifikat als '3Land-Ranger'.\n\n"
            f"Hinweis: Diese Spiellinie wurde didaktisch für {zielgruppe} optimiert."
        )
