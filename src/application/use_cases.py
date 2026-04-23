from src.domain.entities import Spiellinie
from src.domain.value_objects import Zielgruppe, Thema, Prompt
from src.domain.interfaces import ISpiellinienGenerator, IGuardrailService

class GenerateSpiellinie:
    def __init__(self, generator: ISpiellinienGenerator, guardrail: IGuardrailService):
        self.generator = generator
        self.guardrail = guardrail

    def execute(self, zielgruppe_name: str, thema_titel: str) -> Spiellinie:
        zg = Zielgruppe(name=zielgruppe_name)
        thema = Thema(titel=thema_titel)

        # 1. Input Validation
        if not self.guardrail.validate_input(zg, thema):
            raise ValueError("Input validation failed: The requested topic or target group is not allowed.")

        # 2. Prompt Enrichment
        enriched_prompt = self.guardrail.enrich_prompt(zg, thema)

        # 3. KI-Generierung
        raw_content = self.generator.generate(enriched_prompt)

        # 4. Output Verification
        if not self.guardrail.verify_output(raw_content):
            raise ValueError("Unsafe content detected: The generated content violates safety guidelines.")

        # 5. Entity creation
        return Spiellinie(
            zielgruppe=zg,
            thema=thema,
            inhalt=raw_content
        )
