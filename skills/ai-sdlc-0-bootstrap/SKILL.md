---
name: ai-sdlc-0-bootstrap
description: Initialisierung der Projektstruktur und Konfiguration für den Spielliniengenerator.
---

# Phase 0: BOOTSTRAP

Diese Phase dient der Herstellung der Arbeitsfähigkeit. Es werden keine Geschäftslogiken implementiert.

## Instruktionen
1. **Ordnerstruktur prüfen:** Stelle sicher, dass die Verzeichnisse `src/domain`, `src/application`, `src/interface` und `src/infrastructure` sowie die entsprechenden `tests/`-Ordner existieren.
2. **Environment:** Erstelle eine `.env.example` mit Platzhaltern für `DATABASE_URL` und `LLM_API_KEY`.
3. **Dependencies:** Initialisiere die `requirements.txt` mit Basis-Paketen: `fastapi`, `uvicorn`, `pydantic`, `sqlalchemy`, `pytest`, `httpx`.
4. **Dokumentation:** Stelle sicher, dass `README.md` und `AGENTS.md` aktuell sind und die Vision des 3LandSpiel-Generators widerspiegeln.
5. **Git:** Initialisiere das Repository (falls nicht geschehen) und erstelle ein `.gitignore` für Python und `.env`.

## Outcome
Ein leeres, aber lauffähiges Projektgerüst, das bereit für die Spezifikation ist.
