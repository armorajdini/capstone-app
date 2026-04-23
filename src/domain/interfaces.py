from abc import ABC, abstractmethod
from src.domain.entities import Spiellinie
from src.domain.value_objects import Zielgruppe, Thema, Prompt

class ISpiellinienGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: Prompt) -> str:
        """Generiert eine Spiellinie basierend auf einem Prompt."""
        pass

class IGuardrailService(ABC):
    @abstractmethod
    def validate_input(self, zielgruppe: Zielgruppe, thema: Thema) -> bool:
        """Prüft, ob die Eingaben zulässig sind."""
        pass

    @abstractmethod
    def enrich_prompt(self, zielgruppe: Zielgruppe, thema: Thema) -> Prompt:
        """Erstellt einen sicheren und didaktisch wertvollen Prompt."""
        pass

    @abstractmethod
    def verify_output(self, raw_content: str) -> bool:
        """Prüft den generierten Inhalt auf Qualität und Sicherheit."""
        pass
