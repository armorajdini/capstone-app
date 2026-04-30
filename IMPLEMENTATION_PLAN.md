# Gap-Analyse & Umsetzungsplan (Roadmap)

## 1. Gap-Analyse
Basierend auf der Überprüfung des aktuellen Code-Standes (`capstone-app`) im Vergleich zu den Projekt-Zielvorgaben und dem Referenzprojekt (`BAIssue`) wurden folgende Erkenntnisse gewonnen:

### ✅ Erfüllte Vorgaben:
- **Enterprise-grade Architektur:** Clean Architecture (Domain, Application, Interface, Infrastructure) ist sauber implementiert (`src/domain`, `src/application`, etc.).
- **Entitäten:** Es existieren 7 Entitäten (`User`, `Zielgruppe`, `Thema`, `Aufgabe`, `Station`, `Lernziel`, `Spiellinie`). *Vorgabe (Min. 5) übertroffen.*
- **Use Cases:** Es gibt 2 klar definierte Use Cases (`GenerateSpiellinie`, `GetSpiellinieLibrary`). *Vorgabe (Min. 2) erfüllt.*
- **Datenbank & ORM:** SQLAlchemy wird als ORM genutzt (`src/infrastructure/models.py`). Relationen sind definiert.
- **REST API:** FastAPI stellt `/generate` und `/library` bereit, inkl. automatischer OpenAPI/Swagger-Dokumentation.
- **TDD:** Unit-, Integration- und E2E-Tests sind vorhanden (`tests/`).
- **CD & Docker:** `cd-render.yml`, `release.yml` und `Dockerfile` sind funktionsfähig und vorhanden.

### ❌ Identifizierte Gaps (Was fehlt?):
1. **Web-GUI (Frontend):** Es fehlt die komplette Weboberfläche. Das Referenzprojekt nutzt statische Dateien (`static/index.html`), die via FastAPI ausgeliefert werden. Unser Code-Stand besitzt keine Frontend-Dateien.
2. **Backend-Frontend-Integration:** FastAPI ist momentan ein reines API-Backend (`src/interface/api.py`). Das Ausliefern von statischen Dateien (`StaticFiles` Mount) fehlt noch.
3. **CI-Pipeline (Continuous Integration):** Die Datei `.github/workflows/ci.yml` ist aktuell komplett leer (0 Bytes). Eine automatisierte Testausführung via GitHub Actions ist nicht gegeben.

---

## 2. Priorisierter Umsetzungsplan (Roadmap)

Die Umsetzung erfolgt in vier iterativen Meilensteinen, welche die noch fehlenden Komponenten abdecken.

### Meilenstein 1: CI Pipeline (Foundation) etablieren ✅
*Status: Abgeschlossen*
- [x] Task 1.1: `.github/workflows/ci.yml` geschrieben.

### Meilenstein 2: Web-GUI (Frontend) entwickeln ✅
*Status: Abgeschlossen*
- [x] Task 2.1: Struktur anlegen (`src/interface/static/`).
- [x] Task 2.2: `index.html` (inkl. CSS/JS) erstellt.

### Meilenstein 3: Backend für Web-GUI konfigurieren ✅
*Status: Abgeschlossen*
- [x] Task 3.1: `src/interface/api.py` angepasst (StaticFiles Mount).

### Meilenstein 4: Validierung & Feinschliff ✅
*Status: Abgeschlossen*
- [x] Task 4.1: Frontend API-Verknüpfung getestet.
- [x] Task 4.2: Testsuite (E2E/Integration) erweitert.
- [x] Task 4.3: README.md aktualisiert.