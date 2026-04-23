import uuid
from dataclasses import dataclass, field
from src.domain.value_objects import Zielgruppe, Thema

@dataclass
class Spiellinie:
    zielgruppe: Zielgruppe
    thema: Thema
    inhalt: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
