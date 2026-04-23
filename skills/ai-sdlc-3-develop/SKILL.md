---
name: ai-sdlc-3-develop
description: Testgetriebene Entwicklung (TDD) der Applikationslogik und APIs.
---

# Phase 3: DEVELOP

In dieser Phase schreiben wir den Code. Wir folgen dabei strikt dem TDD-Zyklus aus `docs/TDD.md`.

## Strikte Regeln
1. **No Code without Test:** Implementiere keine Geschäftslogik, ohne vorher einen fehlschlagenden Unit-Test geschrieben zu haben.
2. **Layer-By-Layer:**
   - **Domain:** Starte mit Entities und Interfaces.
   - **Application:** Implementiere den `GuardrailService` und die Usecases. Mocke dabei das LLM-Interface.
   - **Interface:** Implementiere die FastAPI Router.
   - **Infrastructure:** Implementiere das `SQLAlchemyRepository` und den `MockLLMAdapter`.
3. **Dependency Inversion:** Stelle sicher, dass der Application-Layer niemals direkt `openai` oder ähnliche Libraries importiert.

## Fokus: Guardrail-Entwicklung
- Teste den Guardrail-Service isoliert:
  - Schlägt er fehl bei bösartigem Input? (Blacklisting)
  - Reichert er den Prompt korrekt an? (Context Injection)
  - Validiert er das Antwortformat des LLMs? (Output Parsing)

## Outcome
Ein funktionaler, vollständig durch Tests abgesicherter Codebase.
