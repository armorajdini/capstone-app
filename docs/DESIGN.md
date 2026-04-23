# Software-Architektur: KI-gestützter Spielliniengenerator

## 1. Clean Architecture Mapping

Die Anwendung folgt dem Prinzip der Clean Architecture, um die Geschäftslogik von technischen Details zu entkoppeln.

### Domain Layer (Kern)
*   **Entities:** `Spiellinie` (Repräsentiert das generierte Ergebnis).
*   **Value Objects:** `Zielgruppe`, `Thema`, `Prompt`.
*   **Interfaces:** `ISpiellinienGenerator` (Port für das LLM), `IGuardrailService` (Port für Sicherheitsprüfungen).

### Application Layer (Use Cases)
*   **Use Case:** `GenerateSpiellinie` koordiniert den Ablauf.
*   **Guardrail-Layer:** Hier liegt die Implementierung der Sicherheits- und Didaktik-Logik. Sie stellt sicher, dass Eingaben validiert und Prompts angereichert werden, bevor sie den Domain-Kern verlassen.
*   **DTOs:** `GenerateSpiellinieRequest`, `SpiellinieResponse`.

### Interface Layer (Adapters)
*   **Web API:** FastAPI Controller, die HTTP-Requests in Application-Calls übersetzen.
*   **CLI:** (Optional) Ein Kommandozeilen-Interface für Administratoren.

### Infrastructure Layer (External Agency)
*   **LLM Adapter:** Konkrete Implementierung für OpenAI, Anthropic oder lokale Modelle.
*   **Persistence:** PostgreSQL via SQLAlchemy für das Speichern generierter Spiellinien.
*   **Logging/Monitoring:** Tracking von Guardrail-Verstößen.

---

## 2. Der Guardrail-Layer

Der **Guardrail-Layer** ist als Service innerhalb der **Application-Schicht** platziert. Er fungiert als "Torwächter" (Gatekeeper) zwischen dem Benutzer-Input und dem LLM-Aufruf.

### Funktionsweise
1.  **Input Validation:** Prüfung auf schädliche Inhalte oder unzulässige Themen (Blacklisting).
2.  **Context Injection:** Anreicherung des Benutzer-Prompts mit einem "System-Prompt", der die didaktischen Leitplanken (z.B. "Du bist ein Experte für Erlebnispädagogik im 3Land...") definiert.
3.  **Output Verification:** Prüfung der LLM-Antwort auf Konsistenz und Einhaltung der Formate (z.B. JSON-Struktur) vor der Rückgabe an das UI.

Dies kapselt das Risiko, da das LLM niemals "rohe" Benutzerdaten erhält und die Antwort einer finalen Qualitätskontrolle unterliegt.

---

## 3. Tech-Stack

*   **Backend:** Python 3.11+ mit **FastAPI**.
*   **KI-Orchestrierung:** **LangChain** oder **Semantic Kernel** zur Verwaltung der Guardrail-Chains.
*   **Datenbank:** **PostgreSQL** mit **SQLAlchemy** (Core & ORM).
*   **Migrationen:** **Alembic**.
*   **Validation:** **Pydantic v2**.
*   **Deployment:** **Docker** & Docker Compose.

---

## 4. Test-Strategie (Test-Pyramide)

### Unit Tests
*   Fokus: Einzelne Logik-Bausteine des Guardrail-Layers (z.B. Prompt-Template-Generierung).
*   Tool: `pytest`.

### Integration Tests
*   Fokus: Zusammenspiel von Application Layer und Infrastructure (z.B. Persistenz in Test-DB).
*   Mocking: LLM-Antworten werden hier gemockt, um Kosten und Flakiness zu vermeiden.

### E2E Tests
*   Fokus: Vollständiger Durchlauf vom API-Endpoint bis zur (simulierten) KI-Antwort.
*   Strategie: Verwendung von **VCR.py** oder **HTTPX**, um reale LLM-Interaktionen für Regressionstests aufzuzeichnen und wiederzugeben.
*   Validierung der UI-Sichtbarkeit des Ergebnisses.
