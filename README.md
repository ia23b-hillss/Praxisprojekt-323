# Flask Text Analyzer - Praxisprojekt Modul 323

Eine Flask-Applikation zur Textanalyse mit funktionaler Programmierung.

## Installation

1. Installieren Sie die Dependencies:
```bash
pip install -r requirements.txt
```

## Starten der Anwendung

```bash
python app.py
```

Die Anwendung läuft dann auf `http://localhost:5000`

## Projektstruktur

```
Praxisprojekt-323/
├── app.py                  # Haupt-Flask-Applikation
├── text_analyzer.py        # Funktionale Textverarbeitungs-Logik
├── functional_utils.py      # Höherwertige Funktionen und Utilities
├── requirements.txt        # Python Dependencies
├── templates/
│   └── index.html         # Web-Interface
└── static/
    └── style.css          # CSS Styling
```

## Funktionen

Die Anwendung bietet folgende Funktionen:

- **Textanalyse**: Statistische Analyse von Texten (Wörter, Zeichen, Sätze, etc.)
- **Text-Transformation**: Transformationen mit höherwertigen Funktionen
- **Text-Filterung**: Filterung mit Lambda-Ausdrücken und funktionalen Methoden
- **Lambda-Demo**: Demonstration von Lambda-Ausdrücken
- **Map/Filter/Reduce Demo**: Demonstration funktionaler Datenverarbeitung

## Abgedeckte Kompetenzfelder

Alle 18 Kompetenzfelder des Moduls 323 sind implementiert:

- **A1G, A1F, A1E**: Pure functions, immutable values, Paradigmen-Vergleich
- **B1G, B1F, B1E**: Algorithmen-Erklärung, Zerlegung, Implementierung
- **B2G, B2F, B2E**: Funktionen als Objekte, höherwertige Funktionen, Closures
- **B3G, B3F, B3E**: Einfache Lambdas, mehrere Argumente, Programmfluss
- **B4G, B4F, B4E**: Map/Filter/Reduce einzeln, kombiniert, komplex
- **C1G, C1F, C1E**: Refactoring-Techniken, Anwendung, Auswirkungen

## Code-Beispiele für Portfolio

Alle Code-Beispiele für die Lernnachweise finden Sie in:
- `text_analyzer.py`: Pure functions, Map/Filter/Reduce, Lambda-Ausdrücke, Refactoring
- `functional_utils.py`: Höherwertige Funktionen, Closures, Funktionen als Objekte


