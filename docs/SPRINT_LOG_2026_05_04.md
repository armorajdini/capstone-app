# Sprint Log: Cloud Deployment & Persistence (2026-05-04)

## Übersicht
In diesem Sprint wurde die Anwendung von einer rein lokalen Entwicklungsumgebung in eine professionelle Cloud-Infrastruktur überführt. Die Anwendung ist nun weltweit über eine URL erreichbar und speichert Daten dauerhaft in einer Cloud-Datenbank.

## Durchgeführte Änderungen

### 1. Cloud-Datenbank (Neon Postgres)
- **Tool:** [Neon.tech](https://neon.tech) (Serverless Postgres).
- **Status:** Aktiv und verbunden.
- **Vorteil:** Daten bleiben auch nach Server-Neustarts erhalten (persistente Speicherung).

### 2. Cloud-Hosting (Render)
- **Tool:** [Render.com](https://render.com).
- **Methode:** Docker-Deployment basierend auf Branch `test_ms_v1`.
- **URL:** `https://capstone-app-jnin.onrender.com`
- **Konfiguration:** Environment Variable `DATABASE_URL` für die sichere Verbindung zur DB hinterlegt.

### 3. Code-Anpassungen (Infrastructure Layer)
- **`requirements.txt`**: `psycopg2-binary` hinzugefügt (Postgres-Treiber).
- **`src/infrastructure/database.py`**: Multi-DB Support implementiert. Erkennt automatisch, ob SQLite (lokal) oder Postgres (Cloud) genutzt wird.
- **`src/infrastructure/config.py`**: Dynamische URL-Verarbeitung implementiert, um Render- und Neon-Konfigurationen abzufangen.

## Aktueller Status
- **Backend:** Live auf Render.
- **Datenbank:** Live auf Neon.
- **Verbindung:** Erfolgreich getestet (Einträge über GUI werden in Neon gespeichert).
- **KI-Modul:** Aktuell noch `MockLLM` (Simulator). Der nächste logische Schritt wäre die Integration von LiteLLM für echte KI-Generierung.

## Anleitung für das Team
Um die Cloud-DB lokal zu nutzen (Vorsicht: verändert die echten Daten!), müsste die `DATABASE_URL` in einer lokalen `.env` Datei eingetragen werden. Standardmäßig nutzt die App lokal weiterhin die `3landspiel_v2.db`.
