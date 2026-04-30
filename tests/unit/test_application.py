import pytest
from unittest.mock import MagicMock
from src.domain.entities import Spiellinie
from src.domain.value_objects import Zielgruppe, Thema, Prompt
from src.domain.interfaces import ISpiellinienGenerator, ISpiellinieRepository
from src.application.use_cases import GenerateSpiellinie
from src.application.services import GuardrailService

@pytest.fixture
def mock_generator():
    return MagicMock(spec=ISpiellinienGenerator)

@pytest.fixture
def mock_repository():
    return MagicMock(spec=ISpiellinieRepository)

@pytest.fixture
def guardrail_service():
    return GuardrailService()

def test_guardrail_enrich_prompt(guardrail_service):
    zg = Zielgruppe(name="Primarschule")
    thema = Thema(titel="Rhein-Abenteuer")
    
    enriched_prompt = guardrail_service.enrich_prompt(zg, thema)
    
    assert "Primarschule" in enriched_prompt.text
    assert "Rhein-Abenteuer" in enriched_prompt.text
    assert "3LandSpiel" in enriched_prompt.text

def test_guardrail_validate_input_valid(guardrail_service):
    zg = Zielgruppe(name="Primarschule")
    thema = Thema(titel="Natur am Rhein")
    assert guardrail_service.validate_input(zg, thema) is True

def test_guardrail_validate_input_invalid_topic(guardrail_service):
    zg = Zielgruppe(name="Primarschule")
    thema = Thema(titel="Extremismus im 3Land")
    assert guardrail_service.validate_input(zg, thema) is False

def test_guardrail_validate_input_invalid_target_group(guardrail_service):
    zg = Zielgruppe(name="Hacker")
    thema = Thema(titel="Natur am Rhein")
    assert guardrail_service.validate_input(zg, thema) is False

def test_guardrail_verify_output_too_short(guardrail_service):
    assert guardrail_service.verify_output("Zu kurz") is False

def test_guardrail_verify_output_unsafe(guardrail_service):
    content = "Dies ist ein sehr langer Text, der aber leider von Gewalt handelt und daher abgelehnt werden muss."
    assert guardrail_service.verify_output(content) is False

def test_use_case_happy_path(mock_generator, guardrail_service, mock_repository):
    use_case = GenerateSpiellinie(generator=mock_generator, guardrail=guardrail_service, repository=mock_repository)
    mock_generator.generate.return_value = "Dies ist eine sehr lange und absolut sichere Spiellinie, die alle Kriterien erfüllt."
    
    result = use_case.execute("Primarschule", "Natur am Rhein", user_name="Test Lehrer")
    
    assert isinstance(result, Spiellinie)
    assert "sichere Spiellinie" in result.inhalt
    assert len(result.stationen) == 1
    mock_generator.generate.assert_called_once()
    mock_repository.save.assert_called_once()
