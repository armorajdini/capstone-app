import pytest
from src.domain.entities import Spiellinie
from src.domain.value_objects import Zielgruppe, Thema, Prompt

def test_zielgruppe_creation():
    zg = Zielgruppe(name="Primarschule")
    assert zg.name == "Primarschule"

def test_zielgruppe_invalid_name():
    with pytest.raises(ValueError):
        Zielgruppe(name="")

def test_thema_creation():
    t = Thema(titel="Umweltschutz am Rhein")
    assert t.titel == "Umweltschutz am Rhein"

def test_thema_invalid_titel():
    with pytest.raises(ValueError):
        Thema(titel="a" * 2)  # Too short

def test_prompt_creation():
    p = Prompt(text="Erstelle eine Geschichte...")
    assert p.text == "Erstelle eine Geschichte..."

def test_spiellinie_creation():
    zg = Zielgruppe(name="Primarschule")
    thema = Thema(titel="Umweltschutz")
    inhalt = "Dies ist eine spannende Geschichte..."
    
    sl = Spiellinie(zielgruppe=zg, thema=thema, inhalt=inhalt)
    
    assert sl.zielgruppe == zg
    assert sl.thema == thema
    assert sl.inhalt == inhalt
    assert sl.id is not None
