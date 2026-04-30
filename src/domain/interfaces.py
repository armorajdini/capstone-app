from abc import ABC, abstractmethod
from src.domain.value_objects import Zielgruppe, Thema, Prompt
from src.domain.entities import Spiellinie
from typing import List, Optional
from uuid import UUID

class ISpiellinienGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: Prompt) -> str:
        pass

class IGuardrailService(ABC):
    @abstractmethod
    def validate_input(self, zielgruppe: Zielgruppe, thema: Thema) -> bool:
        pass
    
    @abstractmethod
    def enrich_prompt(self, zielgruppe: Zielgruppe, thema: Thema) -> Prompt:
        pass
        
    @abstractmethod
    def verify_output(self, raw_content: str) -> bool:
        pass

class ISpiellinieRepository(ABC):
    @abstractmethod
    def save(self, spiellinie: Spiellinie) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Spiellinie]:
        pass

    @abstractmethod
    def get_by_id(self, spiellinie_id: UUID) -> Optional[Spiellinie]:
        pass
