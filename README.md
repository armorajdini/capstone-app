# KI-gestützter Spielliniengenerator für das 3LandSpiel (Extended MVP)

## 1. Projektübersicht & Scope
Dieses Projekt dient als **erweiterter Prototyp** zur automatisierten Generierung und Verwaltung von Spiellinien für das "3LandSpiel". 

### Kern-Features:
- **Web-GUI:** Intuitive Weboberfläche zur Generierung und Einsicht von Spiellinien.
- **7-Entitäten-Modell:** Vollständige Abbildung von Usern, Zielgruppen, Themen, Spiellinien, Stationen, Aufgaben und Lernzielen.
- **Guardrail-Layer:** Automatisierte Prüfung und Anreicherung der Prompts zur Sicherstellung didaktischer Qualität und Sicherheit.
- **Persistence:** Relationale Speicherung aller generierten Spiellinien in einer SQLite-Datenbank via SQLAlchemy ORM.
- **Library-Funktion:** Abruf und Einsicht aller gespeicherten Spiellinien über einen dedizierten API-Endpunkt.

## 2. Architektur (Clean Architecture)
Das Projekt folgt strikt der **Clean Architecture**:

- **Domain Layer (`src/domain`):** Enthält die 7 Kern-Entities und definiert die Schnittstellen für Generierung und Persistenz.
- **Application Layer (`src/application`):** Beinhaltet die Use Cases (`GenerateSpiellinie`, `GetSpiellinieLibrary`) und den Guardrail-Service.
- **Interface Layer (`src/interface`):** REST-API mittels FastAPI (Swagger UI unter `/docs`) und Web-GUI (ausgeliefert via `/`).
- **Infrastructure Layer (`src/infrastructure`):** Datenbank-Konfiguration (SQLite/ORM) und LLM-Adapter (Mock-LLM).

## 3. Setup & Ausführung

### Lokal starten
```bash
# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
python -m src.main
```
Anschliessend: 
- **Web-GUI:** [http://localhost:8000](http://localhost:8000)
- **API-Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

### Test-Pyramide
```bash
# Alle Tests ausführen
pytest
```

## 4. Datenmodell (ER-Diagramm Logik)
Das System verwaltet folgende Relationen:
- Ein **User** erstellt mehrere **Spiellinien**.
- Eine **Spiellinie** ist verknüpft mit einer **Zielgruppe** und einem **Thema**.
- Eine **Spiellinie** besteht aus mehreren **Stationen**.
- Jede **Station** hat genau eine **Aufgabe**.
- Eine **Spiellinie** kann mehrere **Lernziele** verfolgen.
