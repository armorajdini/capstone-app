---
name: ai-sdlc-2-design
description: Erstellung des technischen Designs unter Berücksichtigung der Clean Architecture.
---

# Phase 2: DESIGN

In dieser Phase planen wir die technische Umsetzung basierend auf den Spezifikationen.

## Design-Prinzipien
1. **Clean Architecture:** Halte dich strikt an `docs/CLEAN_ARCH.md`.
2. **Guardrail-First:** Designe den Guardrail-Service so, dass er im Application-Layer lebt und modular erweiterbar ist (z.B. verschiedene Validatoren für Didaktik, Ethik, Format).
3. **Data Modeling:** Definiere die Pydantic-Schemas für Requests und Responses.
4. **Interface Definition:** Lege die Funktionssignaturen für die Domain-Interfaces (Ports) fest.

## Dokumentation
- Aktualisiere `docs/DESIGN.md` bei Architekturänderungen.
- Erstelle bei Bedarf Sequenzdiagramme (Mermaid) in der Dokumentation, um den Weg vom User-Input über die Guardrails zum LLM zu visualisieren.

## Outcome
Ein klarer Bauplan (Interfaces, Datenmodelle), der direkt in TDD-Tests übersetzt werden kann.
