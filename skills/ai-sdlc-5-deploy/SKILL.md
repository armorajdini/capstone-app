---
name: ai-sdlc-5-deploy
description: Ausrollen des Systems via CI/CD (GitHub Actions) zu Render.
---

# Phase 5: DEPLOY

In dieser Phase automatisieren wir den Release-Prozess.

## CI/CD Pipeline (GitHub Actions)
1. **CI-Workflow:** Bei jedem Push in `main` oder PR werden alle Tests (Unit & Integration) ausgeführt.
2. **Release-Workflow:** Bei Erstellung eines GitHub Releases:
   - Build des Docker-Images.
   - Push des Images zur GitHub Container Registry (GHCR).
3. **CD-Workflow (Manual/Auto):**
   - Trigger eines Webhooks zu **Render.com**, um das neue Image aus GHCR zu ziehen und zu deployen.
   - Durchführung von DB-Migrationen via `alembic upgrade head` im Container.

## Monitoring
- Überprüfe die Logs in Render auf Start-Fehler.
- Validiere die Live-API-Schnittstelle via Swagger UI (z.B. `https://ihre-app.onrender.com/docs`).

## Outcome
Ein live verfügbares System, das kontinuierlich verbessert werden kann.
