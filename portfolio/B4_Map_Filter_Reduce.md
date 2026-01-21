# Lernnachweis zu Kompetenzband B4 (B4G, B4F, B4E)

**Kompetenz**: Funktionale Programmierung umsetzen - Map, Filter und Reduce einzeln anwenden, kombinieren und für komplexe Datenverarbeitung nutzen.

## Einleitung

Map, Filter und Reduce sind die drei Säulen der funktionalen Datenverarbeitung. Diese Konzepte waren für mich zunächst abstrakt, aber im Verlauf meines Praxisprojekts habe ich gelernt, wie mächtig und elegant sie sind. Sie ermöglichen es mir, Daten zu transformieren, zu filtern und zu aggregieren, ohne explizite Schleifen zu verwenden. Mein Text Analyzer Projekt bot die perfekte Gelegenheit, diese Konzepte praktisch anzuwenden und ihre Vorteile zu erleben.

## B4G: Map, Filter und Reduce einzeln anwenden

Map, Filter und Reduce sind drei fundamentale Funktionen der funktionalen Programmierung. Map transformiert jedes Element einer Liste, Filter selektiert Elemente basierend auf einer Bedingung, und Reduce aggregiert alle Elemente zu einem einzigen Wert.

In meinem Projekt habe ich jede dieser Funktionen einzeln implementiert und verwendet, um verschiedene Textverarbeitungsaufgaben zu lösen.

**Code-Beispiel B4G - Map, Filter, Reduce einzeln:**

```python
def transform_words_map(text: str, transformation: Callable[[str], str]) -> List[str]:
    """
    B4G: Map einzeln anwenden
    Transformiert jedes Wort mit einer Funktion
    """
    words = text.split()
    return list(map(transformation, words))

def filter_words_by_length(text: str, min_length: int) -> List[str]:
    """
    B4G: Filter einzeln anwenden
    Filtert Wörter nach Mindestlänge
    """
    words = text.split()
    return list(filter(lambda w: len(w) >= min_length, words))

def calculate_total_word_length_reduce(text: str) -> int:
    """
    B4G: Reduce einzeln anwenden
    Berechnet Gesamtlänge aller Wörter
    """
    words = text.split()
    if not words:
        return 0
    return reduce(lambda acc, w: acc + len(w), words, 0)
```

Diese Beispiele zeigen die grundlegende Verwendung jeder Funktion: `transform_words_map()` verwendet Map, um jedes Wort zu transformieren, `filter_words_by_length()` verwendet Filter, um Wörter nach Länge zu selektieren, und `calculate_total_word_length_reduce()` verwendet Reduce, um die Gesamtlänge aller Wörter zu berechnen.

Der Vorteil dieser Funktionen ist ihre Klarheit und Lesbarkeit. Anstatt eine Schleife zu schreiben, beschreibe ich, was ich will: "Transformiere jedes Element", "Filtere Elemente" oder "Reduziere alle Elemente zu einem Wert". Dies macht den Code deklarativer und oft auch wartbarer.

In meinem Projekt verwende ich diese Funktionen für verschiedene Textverarbeitungsaufgaben. Map für Transformationen wie Groß-/Kleinschreibung, Filter für Selektionen wie lange Wörter, und Reduce für Aggregationen wie Summen oder Durchschnitte.

## B4F: Map, Filter und Reduce kombinieren

Die wahre Stärke von Map, Filter und Reduce zeigt sich, wenn ich sie kombiniere. Durch die Verkettung dieser Funktionen kann ich komplexe Datenverarbeitungspipelines erstellen, die Daten durch mehrere Transformationen schicken.

In meinem Projekt habe ich mehrere Funktionen implementiert, die Map, Filter und Reduce kombinieren, um komplexere Aufgaben zu lösen.

**Code-Beispiel B4F - Map, Filter, Reduce kombiniert:**

```python
def count_long_words_combined(text: str, min_length: int) -> int:
    """
    B4F: Map, Filter und Reduce kombiniert
    Zählt Wörter mit Mindestlänge und summiert deren Längen
    """
    words = text.split()
    if not words:
        return 0
    
    # Kombiniert: Filter -> Map -> Reduce
    long_words = filter(lambda w: len(w) >= min_length, words)
    word_lengths = map(len, long_words)
    total_length = reduce(lambda acc, length: acc + length, word_lengths, 0)
    return total_length
```

Diese Funktion zeigt, wie ich Map, Filter und Reduce kombiniere: Zuerst filtere ich die Wörter nach Mindestlänge, dann transformiere ich sie mit Map zu ihren Längen, und schließlich reduziere ich sie mit Reduce zu einer Summe.

Die Kombination dieser Funktionen ermöglicht es mir, komplexe Datenverarbeitung in einer Pipeline zu beschreiben. Jeder Schritt ist klar definiert, und die Pipeline ist leicht zu verstehen und zu erweitern. Wenn ich zum Beispiel einen weiteren Filter hinzufügen möchte, kann ich dies einfach tun, ohne die gesamte Logik zu ändern.

In meinem Projekt verwende ich kombinierte Map/Filter/Reduce-Operationen für verschiedene Analysen, wie die Berechnung von Statistiken über gefilterte Daten oder die Aggregation von transformierten Werten.

## B4E: Komplexe Datenverarbeitung mit Map, Filter, Reduce

Die erweiterte Anwendung zeigt sich in komplexen Datenverarbeitungsaufgaben, die mehrere Transformationen, Filterungen und Aggregationen kombinieren. Diese Aufgaben erfordern ein tiefes Verständnis davon, wie Map, Filter und Reduce zusammenarbeiten.

In meinem Projekt habe ich komplexe Algorithmen implementiert, die Map, Filter und Reduce für anspruchsvolle Datenverarbeitung verwenden, wie die Analyse von Wortfrequenzen.

**Code-Beispiel B4E - Komplexe Datenverarbeitung:**

```python
def analyze_word_frequencies(text: str) -> Dict[str, int]:
    """
    B4E: Komplexe Datenverarbeitung mit Map, Filter, Reduce
    Erstellt Wörterbuch mit Wortfrequenzen
    """
    words = text.lower().split()
    if not words:
        return {}
    
    # Normalisiere Wörter (entferne Satzzeichen)
    normalized = map(lambda w: w.strip('.,!?;:()[]{}"\''), words)
    # Filtere leere Strings
    valid_words = filter(lambda w: len(w) > 0, normalized)
    
    # Reduziere zu Frequenz-Dictionary
    def update_freq(acc: Dict, word: str) -> Dict:
        acc[word] = acc.get(word, 0) + 1
        return acc
    
    return reduce(update_freq, valid_words, {})

def get_top_words(text: str, top_n: int = 5) -> List[tuple]:
    """
    B4E: Komplexe Transformation - Top N häufigste Wörter
    Verwendet Map, Filter, Reduce für komplette Pipeline
    """
    frequencies = analyze_word_frequencies(text)
    if not frequencies:
        return []
    
    # Sortiere nach Häufigkeit (Reduce für Sortierung)
    sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:top_n]
```

Diese Funktionen zeigen komplexe Datenverarbeitung: `analyze_word_frequencies()` verwendet Map für Normalisierung, Filter für Validierung und Reduce für Aggregation. `get_top_words()` kombiniert dies mit Sortierung, um die häufigsten Wörter zu finden.

Die Komplexität liegt nicht nur in der Kombination der Funktionen, sondern auch in der Art, wie sie zusammenarbeiten. Die Pipeline normalisiert zuerst die Daten, filtert dann ungültige Werte und aggregiert schließlich die Ergebnisse. Jeder Schritt baut auf dem vorherigen auf, was eine klare Datenfluss-Logik schafft.

In meinem Projekt verwende ich solche komplexen Pipelines für verschiedene Analysen, wie die Identifikation von Schlüsselwörtern, die Berechnung von Statistiken über gefilterte Daten oder die Transformation von Datenstrukturen.

## Lernprozess und Reflexion

Map, Filter und Reduce waren für mich zunächst abstrakte Konzepte, die ich nur aus theoretischen Kontexten kannte. Die praktische Anwendung in meinem Projekt war entscheidend für mein Verständnis.

Was mir besonders geholfen hat, war die schrittweise Einführung: Zuerst lernte ich jede Funktion einzeln, dann kombinierte ich sie, und schließlich verwendete ich sie für komplexe Aufgaben. Diese schrittweise Herangehensweise machte die Konzepte greifbarer.

Die größte Herausforderung war, zu verstehen, wie ich Map, Filter und Reduce kombiniere, um komplexe Aufgaben zu lösen. Besonders die Verwendung von Reduce für Aggregationen war am Anfang verwirrend, da ich gewohnt war, Schleifen zu verwenden.

Besonders wertvoll war die Erkenntnis, dass Map, Filter und Reduce den Code deklarativer machen. Anstatt zu beschreiben, wie ich Daten verarbeite, beschreibe ich, was ich will. Dies macht den Code oft lesbarer und wartbarer.

Die Verwendung für komplexe Datenverarbeitung war am Anfang schwierig, besonders bei verschachtelten Transformationen. Mit der Zeit wurde es jedoch natürlicher, und ich lernte, wie ich Pipelines aus Map, Filter und Reduce erstelle, um komplexe Aufgaben zu lösen.

## Zukünftige Schritte

Ich plane, mein Wissen über Map, Filter und Reduce weiter zu vertiefen, insbesondere durch die Anwendung in komplexeren Datenverarbeitungsszenarien. Besonders interessiert mich, wie ich diese Funktionen für die Verarbeitung großer Datenmengen optimieren kann und wie ich sie parallelisiere.

Ich möchte auch lernen, wie ich Map, Filter und Reduce für die Verarbeitung von verschachtelten Datenstrukturen verwende und wie ich sie mit anderen funktionalen Konzepten kombiniere. Die Fähigkeit, komplexe Datenverarbeitung mit Map, Filter und Reduce zu implementieren, wird mir in zukünftigen Projekten sehr nützlich sein, besonders in Bereichen wie Datenanalyse und API-Entwicklung.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher im Umgang mit Map, Filter und Reduce für einfache Operationen, kombinierte Pipelines und komplexe Datenverarbeitung. Diese Konzepte haben meine Fähigkeit, elegante und wartbare Datenverarbeitung zu implementieren, erheblich verbessert.


