# KI-gestützter Spielliniengenerator für das 3LandSpiel (MVP)

## 1. Projektübersicht & Scope
Dieses Projekt dient als **MVP (Minimum Viable Product)** zur automatisierten Generierung von Spiellinien für das "3LandSpiel". 

### Wichtige Scope-Abgrenzung:
- **Interaction:** Die Interaktion erfolgt ausschliesslich über die **FastAPI Swagger UI** (`/docs`). Ein Web-Frontend ist für diesen Prototypen **Out-of-Scope**.
- **Persistenz:** Eine Datenbank-Persistenz ist in diesem initialen MVP **nicht implementiert**. Generierte Spiellinien werden flüchtig verarbeitet und direkt zurückgegeben.
- **LLM:** Zur Demonstration wird ein **Mock-LLM** verwendet, welches plausible Ergebnisse basierend auf den Eingabeparametern simuliert.

**Kern-Use-Case (UC-001):**
- Eingabe von Zielgruppe (z.B. Primarschule) und Thema (z.B. Rhein-Ökologie).
- Automatisierte Prüfung und Anreicherung des Prompts durch einen **Guardrail-Layer**.
- Generierung und Rückgabe der Spiellinie als strukturierte API-Antwort.

## 2. Architektur (Clean Architecture)
Der Code ist strikt nach der **Clean Architecture** organisiert, um Geschäftslogik von technischer Infrastruktur zu trennen:

- **Domain Layer (`src/domain`):** Enthält Core-Entities (`Spiellinie`) und Value Objects. Definiert die Schnittstellen (Interfaces) für externe Dienste.
- **Application Layer (`src/application`):** Orchestriert die Use-Cases und enthält den **Guardrail-Service** (Input-Validierung, Prompt-Enrichment, Output-Verifizierung).
- **Interface Layer (`src/interface`):** Stellt die REST-API mittels FastAPI bereit.
- **Infrastructure Layer (`src/infrastructure`):** Beinhaltet die Konfiguration (`config.py`) und den LLM-Adapter (Mock-LLM).

## 3. Setup & Ausführung

### Start via Docker
```bash
docker build -t capstone-app .
docker run -p 8000:8000 capstone-app
```
Anschliessend: [http://localhost:8000/docs](http://localhost:8000/docs)

### Test-Pyramide
```bash
# Unit & Integration
export PYTHONPATH=$PYTHONPATH:. && pytest tests/unit tests/integration

# E2E (erfordert laufende App)
pytest tests/e2e/test_e2e.py
```

## 4. AI-SDLC Workflow
Dieses Projekt folgt einem **AI-Assisted Lean SDLC**. 
**Hinweis zu Platzhaltern:** Im Verzeichnis `skills/` oder unter `docs/` befindliche, nahezu leere Markdown-Dateien (z.B. `SKILL.md`) dienen bewusst als **strukturelle Platzhalter**. Sie demonstrieren das Konzept des "Progressive Disclosure" für Agentic AI – die Struktur ist definiert, der Inhalt wird bei Bedarf durch spezialisierte Agenten expandiert.

Phasen:
- **0-BOOTSTRAP:** Initialisierung der Projektstruktur.
- **1-SPECIFY:** Anforderungsdefinition (`docs/specs/`).
- **2-DESIGN:** Architektur-Blueprint (`docs/DESIGN.md`).
- **3-DEVELOP:** TDD-Implementierung (Red-Green-Refactor).
- **4-VALIDATE:** Qualitätssicherung via Test-Pyramide.
- **5-DEPLOY:** Containerisierung und CI/CD-Setup.
