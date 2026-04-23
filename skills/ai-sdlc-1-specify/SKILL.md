---
name: ai-sdlc-1-specify
description: Erstellung und Verfeinerung von Use Cases für den Spielliniengenerator.
---

# Phase 1: SPECIFY

In dieser Phase definieren wir präzise, WAS gebaut wird, ohne das WIE vorwegzunehmen.

## Regeln für Use Cases (Markdown)
1. **Dateiname:** Nutze das Format `docs/specs/UC-XXX.md`.
2. **Struktur:** Jeder Use Case muss folgende Sektionen enthalten:
   - **Kurzbeschreibung:** Ein Satz zum Ziel.
   - **Akteure:** Wer interagiert mit dem System?
   - **Vorbedingungen:** Was muss gegeben sein?
   - **Standardablauf (Happy Path):** Nummerierte Schritte.
   - **Alternative Abläufe:** Was passiert bei Fehlern oder Abweichungen?
   - **Akzeptanzkriterien:** Checkliste für die spätere Validierung.
3. **Fokus:** Betone bei KI-Features explizit die Rolle des Guardrail-Layers (z.B. "System validiert Prompt gegen pädagogische Richtlinien").

## Aufgaben
- Überprüfe `docs/specs/UC-001.md` auf Vollständigkeit.
- Identifiziere weitere MVPs (z.B. UC-002: Spiellinie speichern, UC-003: Verlauf einsehen).

## Outcome
Abgenommene Spezifikationen, die als Grundlage für das Design dienen.
