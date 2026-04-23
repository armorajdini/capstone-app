# Clean Architecture Regeln

Dieses Projekt folgt strikt den Prinzipien der Clean Architecture (Onion Architecture). Ziel ist die Unabhängigkeit von Frameworks, Datenbanken und externen APIs (wie LLMs).

## Die 4 Schichten

### 1. Domain Layer (Kern)
- **Inhalt:** Enthält reine Geschäftslogik, Entities und Value Objects.
- **Regel:** Darf KEINE Abhängigkeiten zu anderen Schichten haben.
- **Wichtig:** Hier werden Interfaces (Abstraktionen) für externe Dienste definiert (z.B. `ISpiellinienGenerator`).

### 2. Application Layer (Usecases)
- **Inhalt:** Orchestriert den Datenfluss zu und von den Entities. Enthält Usecases und Services.
- **Guardrail-Layer:** Die Sicherheits- und Didaktik-Logik liegt HIER. Sie nutzt Domain-Interfaces, um Logik zu implementieren.
- **Wichtig:** Gemäß **Dependency Inversion** darf dieser Layer keine echten LLM-APIs aufrufen. Er arbeitet nur gegen Interfaces aus dem Domain Layer.

### 3. Interface Layer (Adapters)
- **Inhalt:** Konvertiert Daten zwischen dem für Usecases/Entities bequemsten Format und dem für externe Agenten (Web, CLI) bequemsten Format.
- **Beispiele:** FastAPI Router, Request/Response Schemas (Pydantic).

### 4. Infrastructure Layer
- **Inhalt:** Enthält die konkreten Implementierungen von Interfaces.
- **Beispiele:** Datenbank-Repositories (SQLAlchemy), LLM-Clients (OpenAI-Wrapper), Logging-Tools.
- **Regel:** Hier fließen die Abhängigkeiten zusammen.

## Goldene Regel der Abhängigkeiten
Abhängigkeiten dürfen nur nach **INNEN** zeigen.
`Infrastructure -> Interface -> Application -> Domain`

## Besonderheit: LLM-Zugriff
Echte LLM-Aufrufe sind "Infrastructure". Der Application-Layer (Guardrail-Service) weiß nicht, ob ein echtes GPT-4 oder ein Mock antwortet. Dies ermöglicht deterministische Tests ohne API-Kosten.
