# Software-Architektur: 3LandSpiel Spielliniengenerator (Extended)

## 1. Clean Architecture Mapping

### Domain Layer (Kern)
- **Entities (7):** `User`, `Zielgruppe`, `Thema`, `Spiellinie`, `Station`, `Aufgabe`, `Lernziel`.
- **Interfaces:** `ISpiellinienGenerator`, `IGuardrailService`, `ISpiellinieRepository`.

### Application Layer (Use Cases)
- **Use Cases:** 
    - `GenerateSpiellinie`: Orchestriert Validierung, Generierung und Persistenz.
    - `GetSpiellinieLibrary`: Verwaltet den Zugriff auf die Datenbank-Historie.
- **Services:** `GuardrailService` zur Absicherung von Input und Output.

### Interface Layer (Adapters)
- **API:** FastAPI mit Pydantic-Validierung. Stellt Swagger-Dokumentation bereit.

### Infrastructure Layer (External Agency)
- **Persistence:** SQLite mit **SQLAlchemy ORM**.
- **Generator:** `MockLLMGenerator` zur stabilen Simulation der KI-Antworten.

---

## 2. Relationales Datenmodell (ORM)

Das System nutzt ein relationales Schema, um die pädagogische Komplexität abzubilden:
- **One-to-Many:** Ein `User` kann viele `Spiellinien` besitzen.
- **One-to-Many:** Eine `Spiellinie` hat mehrere `Stationen`.
- **One-to-One:** Jede `Station` ist fest mit einer `Aufgabe` verknüpft.
- **Many-to-Many:** `Spiellinien` und `Lernziele` sind über eine Verknüpfungstabelle verbunden.
- **Foreign Keys:** `Spiellinie` referenziert eindeutige `Thema`- und `Zielgruppe`-Einträge.

---

## 3. Der Guardrail-Layer

Der **Guardrail-Layer** schützt die Integrität der Anwendung:
1. **Input Validation:** Abgleich des Themas gegen eine konfigurierbare Blacklist (Waffen, Gewalt, etc.).
2. **Prompt Enrichment:** Automatisches Hinzufügen von System-Instruktionen und Kontext zur Zielgruppe.
3. **Output Verification:** Scan der KI-Antwort auf unzulässige Begriffe vor der Speicherung.

---

## 4. Tech-Stack

- **Sprache:** Python 3.12
- **Web-Framework:** FastAPI & Uvicorn
- **ORM:** SQLAlchemy 2.0
- **Datenbank:** SQLite (Lokal)
- **Testing:** Pytest & HTTPX TestClient
