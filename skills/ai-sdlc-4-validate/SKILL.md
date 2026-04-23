---
name: ai-sdlc-4-validate
description: Qualitätssicherung durch Ausführung der vollständigen Test-Pyramide.
---

# Phase 4: VALIDATE

In dieser Phase verifizieren wir, dass das System die Akzeptanzkriterien aus den Use Cases erfüllt.

## Validierungsschritte
1. **Pytest-Lauf:** Führe `pytest` lokal aus. Alle Unit- und Integrationstests müssen grün sein.
2. **Coverage-Check:** Prüfe, ob die Testabdeckung (besonders im Application-Layer) ausreichend ist (> 90%).
3. **Docker-Build:** Baue das Docker-Image lokal: `docker build -t spiellinien-gen .`.
4. **E2E-Check:** Starte den Container und führe die E2E-Tests aus:
   - `docker-compose up -d`
   - `pytest tests/e2e`
5. **Linting & Typing:** Führe `ruff check .` und `mypy src` aus, um statische Code-Qualität sicherzustellen.

## Akzeptanz
Ein Feature gilt erst als "Done", wenn alle Akzeptanzkriterien des zugehörigen Use Cases automatisiert nachgewiesen wurden.

## Outcome
Ein verifiziertes, produktionsreifes System.
