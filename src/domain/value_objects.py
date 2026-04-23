from dataclasses import dataclass

@dataclass(frozen=True)
class Zielgruppe:
    name: str

    def __post_init__(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Zielgruppe name darf nicht leer sein.")

@dataclass(frozen=True)
class Thema:
    titel: str

    def __post_init__(self):
        if len(self.titel) < 3:
            raise ValueError("Thema Titel muss mindestens 3 Zeichen lang sein.")

@dataclass(frozen=True)
class Prompt:
    text: str
