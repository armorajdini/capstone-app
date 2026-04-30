from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import List, Optional

@dataclass
class User:
    id: UUID = field(default_factory=uuid4)
    name: str = "Anonym"
    schule: str = "3Land-Schule"

@dataclass
class Zielgruppe:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    beschreibung: str = ""

@dataclass
class Thema:
    id: UUID = field(default_factory=uuid4)
    titel: str = ""
    beschreibung: str = ""

@dataclass
class Aufgabe:
    id: UUID = field(default_factory=uuid4)
    beschreibung: str = ""
    material: str = "Kein Material"

@dataclass
class Station:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    ort: str = ""
    reihenfolge: int = 0
    aufgabe: Optional[Aufgabe] = None

@dataclass
class Lernziel:
    id: UUID = field(default_factory=uuid4)
    beschreibung: str = ""

@dataclass
class Spiellinie:
    id: UUID = field(default_factory=uuid4)
    inhalt: str = ""
    user: Optional[User] = None
    zielgruppe: Optional[Zielgruppe] = None
    thema: Optional[Thema] = None
    stationen: List[Station] = field(default_factory=list)
    lernziele: List[Lernziel] = field(default_factory=list)
