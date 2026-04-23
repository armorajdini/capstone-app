# Test-Driven Development (TDD) Guide

Wir entwickeln dieses Projekt konsequent nach dem TDD-Prinzip, um höchste Qualität und Wartbarkeit sicherzustellen.

## Der Zyklus: Red - Green - Refactor

1.  **RED:** Schreibe einen fehlschlagenden Test für die kleinste denkbare Einheit an Funktionalität.
2.  **GREEN:** Schreibe gerade so viel Code, dass der Test besteht. Keine "Gold-Plating".
3.  **REFACTOR:** Räume den Code auf (Namensgebung, Struktur), während alle Tests grün bleiben.

## Unsere Test-Pyramide

### 1. Unit Tests (Basis)
- **Ort:** `tests/unit/`
- **Ziel:** Logik der Domain-Entities und der Application-Services (Guardrails).
- **Isolation:** Keine Datenbank, kein Netzwerk, keine echten LLM-Calls. Alles wird gemockt.
- **Speed:** Müssen in Millisekunden laufen.

### 2. Integration Tests (Mitte)
- **Ort:** `tests/integration/`
- **Ziel:** Zusammenspiel zwischen Adaptern (Interface) und Infrastruktur.
- **Beispiele:** Testet FastAPI-Endpunkte gegen den Application-Service, testet Repository-Implementierungen gegen eine SQLite-In-Memory-Datenbank.
- **Wichtig:** LLMs werden auch hier über Mocks simuliert, um Kosten zu sparen.

### 3. E2E Tests (Spitze)
- **Ort:** `tests/e2e/`
- **Ziel:** Validierung des gesamten Systems im Docker-Container.
- **Flow:** Ein Request geht an die API, durchläuft alle Schichten und liefert ein korrektes Ergebnis zurück.
- **Simulation:** Einsatz von `MockLLM` in der Infrastruktur, um realistische Antworten zu garantieren, ohne externe Abhängigkeiten.

## Test-Befehle
- Alle Tests: `pytest`
- Nur Unit-Tests: `pytest tests/unit`
- Mit Coverage: `pytest --cov=src`
