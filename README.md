# KI-gestützter Spielliniengenerator für das 3LandSpiel

## 1. Projektübersicht und Use Case
Dieses Projekt ist eine Full-Stack-Anwendung zur automatisierten Generierung von Spiellinien für das "3LandSpiel". Benutzer (z.B. Lehrpersonen oder Game Master) können grundlegende Parameter wie Zielgruppe und Thema eingeben. Das System nutzt ein Large Language Model (LLM), um daraus kreative, didaktisch wertvolle und sichere Spielinhalte zu erzeugen.

**Kern-Use-Case (UC-001):**
- Eingabe von Zielgruppe (z.B. Primarschule) und Thema (z.B. Rhein-Ökologie).
- Automatisierte Prüfung und Anreicherung des Prompts durch einen Guardrail-Layer.
- Generierung und Anzeige der Spiellinie im UI.

## 2. Architektur-Überblick
Die Anwendung ist nach den Prinzipien der **Clean Architecture** strukturiert, um eine klare Trennung von Geschäftslogik und Infrastruktur zu gewährleisten.

- **Domain Layer:** Enthält die Kern-Entities (`Spiellinie`) und Value Objects (`Zielgruppe`, `Thema`), sowie die Definition der Ports (Interfaces).
- **Application Layer:** Beinhaltet die Use-Case-Orchestrierung und den spezifischen **Guardrail-Layer**. Dieser fungiert als Gatekeeper, validiert den Benutzer-Input gegen Blacklists, reichert den Prompt mit pädagogischen Kontext an und verifiziert den KI-Output auf Sicherheit.
- **Interface Layer:** Stellt die Web-API mittels **FastAPI** bereit.
- **Infrastructure Layer:** Beinhaltet die Adapter für das LLM (Mock-LLM für Entwicklung) und die Persistenz (vorbereitet für **PostgreSQL** via SQLAlchemy).

## 3. Lokales Setup und Testing

### Start via Docker
Um die Anwendung lokal in einem Container zu starten:
```bash
docker build -t capstone-app .
docker run -p 8000:8000 capstone-app
```
Die API ist anschliessend unter `http://localhost:8000/docs` (Swagger UI) erreichbar.

### Test-Pyramide ausführen
Das Projekt folgt einem strikten TDD-Ansatz. Die Tests werden mit `pytest` ausgeführt:
```bash
# Alle Unit- und Integrationstests ausführen
pytest tests/unit tests/integration
```
- **Unit Tests:** Prüfen Domain-Modelle und Application-Services.
- **Integration Tests:** Validieren die FastAPI-Endpoints und das Zusammenspiel der Layer.
- **E2E Tests:** (In `tests/e2e/`) Simulieren vollständige Benutzerinteraktionen gegen die laufende API.

## 4. CI/CD und Deployment
Die Automatisierung erfolgt über GitHub Actions:

- **Release Workflow (`release.yml`):** Wird bei jedem Push eines Tags (z.B. `v1.0.0`) getriggert. Er baut das Docker-Image und pusht es in die **GitHub Container Registry (GHCR)**.
- **CD Workflow (`cd-render.yml`):** Ermöglicht ein manuelles Deployment (Workflow Dispatch) auf die Cloud-Plattform **Render**, basierend auf dem aktuellsten Docker-Image.

## 5. AI-SDLC Workflow
Dieses Projekt wurde unter Anwendung eines **AI-Assisted Lean SDLC** (Software Development Life Cycle) entwickelt. Dabei wurden die Phasen systematisch mit Unterstützung der **Gemini CLI** durchlaufen:

- **0-BOOTSTRAP:** Initialisierung der Projektstruktur und Konfiguration.
- **1-SPECIFY:** Definition der Anforderungen in `docs/specs/`.
- **2-DESIGN:** Erstellung des Architektur-Blueprints in `docs/DESIGN.md`.
- **3-DEVELOP:** Iterative Implementierung der Layer (Domain -> Application -> Interface) mittels TDD (Red-Green-Refactor).
- **4-VALIDATE:** Sicherstellung der Qualität durch die vollständige Test-Pyramide.
- **5-DEPLOY:** Automatisierung der Auslieferung via CI/CD.

Der gesamte Prozess wurde durch spezialisierte Agent-Instruktionen (`AGENTS.md`) und Skills gesteuert, was eine hohe Konsistenz und Codequalität bei minimalem manuellem Overhead ermöglichte.
