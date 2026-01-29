"""
Text Analyzer - Funktionale Textverarbeitungs-Logik
Implementiert alle funktionalen Programmierkonzepte für Modul 323
"""

from functools import reduce
from typing import Dict, List, Callable


# ============================================================================
# A1G: Pure Functions - Funktionen ohne Seiteneffekte
# ============================================================================

def count_words(text: str) -> int:
    """
    Pure function - keine Seiteneffekte, deterministisch
    Zählt die Anzahl Wörter in einem Text.
    """
    if not text.strip():
        return 0
    return len(text.split())


def count_characters(text: str) -> int:
    """
    Pure function - zählt alle Zeichen im Text (inkl. Leerzeichen)
    """
    return len(text)


def count_characters_no_spaces(text: str) -> int:
    """
    Pure function - zählt Zeichen ohne Leerzeichen
    """
    return len(text.replace(' ', ''))


def count_sentences(text: str) -> int:
    """
    Pure function - zählt Sätze basierend auf Satzzeichen
    """
    if not text.strip():
        return 0
    sentence_endings = ['.', '!', '?']
    count = sum(1 for char in text if char in sentence_endings)
    return max(1, count) if text.strip() else 0


def average_word_length(text: str) -> float:
    """
    Pure function - berechnet durchschnittliche Wortlänge
    """
    words = text.split()
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# ============================================================================
# A1F: Immutable Values - Unveränderliche Werte
# ============================================================================

def uppercase_text(text: str) -> str:
    """
    Erstellt neuen String statt Mutation - Original bleibt unverändert
    """
    return text.upper()


def lowercase_text(text: str) -> str:
    """
    Immutable Transformation - erstellt neuen String
    """
    return text.lower()


def capitalize_text(text: str) -> str:
    """
    Immutable Transformation - erstellt neuen String
    """
    return text.capitalize()


def transform_text(text: str, func: Callable[[str], str]) -> str:
    """
    Wrapper für immutable Transformationen
    Nimmt eine Funktion und wendet sie auf Text an, ohne Original zu ändern
    """
    return func(text)


# ============================================================================
# B1G, B1F, B1E: Algorithmen - Zerlegung in funktionale Teilstücke
# ============================================================================

def analyze_text(text: str) -> Dict:
    """
    Haupt-Algorithmus für Textanalyse
    Zerlegt in funktionale Teilstücke (B1F, B1E)
    Jede Berechnung ist eine separate pure function
    """
    return {
        'word_count': count_words(text),
        'character_count': count_characters(text),
        'character_count_no_spaces': count_characters_no_spaces(text),
        'sentence_count': count_sentences(text),
        'average_word_length': round(average_word_length(text), 2),
        'longest_word': find_longest_word(text),
        'shortest_word': find_shortest_word(text)
    }


def find_longest_word(text: str) -> str:
    """
    Pure function - findet das längste Wort
    """
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def find_shortest_word(text: str) -> str:
    """
    Pure function - findet das kürzeste Wort
    """
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)


# ============================================================================
# B4G, B4F, B4E: Map, Filter, Reduce
# ============================================================================

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


# ============================================================================
# B3G, B3F, B3E: Lambda-Ausdrücke
# ============================================================================

def get_simple_lambda_transformations() -> Dict[str, Callable]:
    """
    B3G: Einfache Lambda-Ausdrücke für einzelne Operationen
    """
    return {
        'uppercase': lambda x: x.upper(),
        'lowercase': lambda x: x.lower(),
        'double': lambda x: x * 2,
        'square_length': lambda x: len(x) ** 2
    }


def filter_words_with_lambda(text: str, min_length: int, max_length: int) -> List[str]:
    """
    B3F: Lambda mit mehreren Argumenten (via functools.partial oder Closure)
    Filtert Wörter nach Längenbereich
    """
    words = text.split()
    # Lambda verwendet min_length und max_length aus Closure
    return list(filter(lambda w: min_length <= len(w) <= max_length, words))


def sort_words_by_criteria(text: str, criteria: str = 'length') -> List[str]:
    """
    B3E: Lambda für Programmfluss-Steuerung (Sortierung)
    Sortiert Wörter nach verschiedenen Kriterien
    """
    words = text.split()
    if not words:
        return []
    
    if criteria == 'length':
        # Sortiere nach Länge, dann alphabetisch
        return sorted(words, key=lambda w: (len(w), w))
    elif criteria == 'length_desc':
        # Sortiere nach Länge absteigend
        return sorted(words, key=lambda w: len(w), reverse=True)
    elif criteria == 'alphabetical':
        # Alphabetisch
        return sorted(words, key=lambda w: w.lower())
    else:
        return words


def remove_duplicates_sorted(text: str) -> List[str]:
    """
    B3E: Lambda für komplexe Sortierung und Deduplizierung
    """
    words = text.split()
    if not words:
        return []
    
    # Sortiere nach Länge und alphabetisch, dann entferne Duplikate
    unique_words = []
    seen = set()
    sorted_words = sorted(words, key=lambda w: (len(w), w.lower()))
    
    for word in sorted_words:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            unique_words.append(word)
    
    return unique_words


# ============================================================================
# C1G, C1F, C1E: Refactoring - Prozedural vs. Funktional
# ============================================================================

def count_long_words_procedural(text: str, min_length: int) -> int:
    """
    C1G, C1F, C1E: PROZEDURALE VERSION (Refactoring-Beispiel)
    
    Diese Version verwendet prozedurale Programmierung:
    - Verwendet Schleifen mit Mutation
    - Direkte Manipulation von Variablen
    - Imperative Kontrollstrukturen
    - Schwerer zu testen und zu verstehen
    
    REFACTORING-PROBLEME:
    - Zähler wird mutiert (count += 1)
    - Schleife mit if-Bedingung statt Filter
    - Weniger wiederverwendbar
    - Schwerer zu parallelisieren
    """
    words = text.split()
    count = 0
    for word in words:
        if len(word) >= min_length:
            count = count + 1
    return count


def count_long_words_functional(text: str, min_length: int) -> int:
    """
    C1G, C1F, C1E: FUNKTIONALE VERSION (Refactored)
    
    Diese Version verwendet funktionale Programmierung:
    - Keine Mutation von Variablen
    - Verwendet Filter und Reduce
    - Deklarativ statt imperativ
    - Leichter zu testen und zu verstehen
    
    REFACTORING-VORTEILE:
    - Keine Seiteneffekte
    - Kompositionierbar
    - Wiederverwendbar
    - Leichter zu parallelisieren
    - Bessere Lesbarkeit
    
    AUSWIRKUNGEN DES REFACTORINGS:
    - Code ist kürzer und klarer
    - Keine unerwünschten Nebeneffekte möglich
    - Einfacher zu erweitern (z.B. weitere Filter hinzufügen)
    - Bessere Testbarkeit (pure function)
    """
    words = text.split()
    return reduce(
        lambda acc, w: acc + 1,
        filter(lambda w: len(w) >= min_length, words),
        0
    )


def process_text_procedural(text: str, min_length: int = 5) -> Dict:
    """
    C1E: PROZEDURALE VERSION - Komplexe Textverarbeitung
    
    REFACTORING-PROBLEME:
    - Viele verschachtelte if-Statements
    - Mutation von result-Dictionary
    - Schwer zu testen (viele Seiteneffekte)
    - Schwer zu erweitern
    """
    result = {}
    words = text.split()
    
    # Zähle Wörter
    result['word_count'] = len(words)
    
    # Finde längstes Wort
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    result['longest_word'] = longest
    
    # Berechne Durchschnitt
    total = 0
    for word in words:
        total = total + len(word)
    if len(words) > 0:
        result['average'] = total / len(words)
    else:
        result['average'] = 0
    
    # Filtere lange Wörter
    long_words = []
    for word in words:
        if len(word) >= min_length:
            long_words.append(word)
    result['long_words'] = long_words
    
    return result


def process_text_functional(text: str, min_length: int = 5) -> Dict:
    """
    C1E: FUNKTIONALE VERSION - Refactored
    
    REFACTORING-VORTEILE:
    - Verwendet pure functions
    - Komposition statt Mutation
    - Leichter zu testen
    - Bessere Lesbarkeit
    - Wiederverwendbare Komponenten
    
    AUSWIRKUNGEN:
    - Keine unerwünschten Nebeneffekte
    - Einfacher zu erweitern
    - Bessere Wartbarkeit
    - Funktionen können isoliert getestet werden
    """
    words = text.split()
    
    return {
        'word_count': len(words),
        'longest_word': max(words, key=len) if words else "",
        'average': sum(map(len, words)) / len(words) if words else 0,
        'long_words': list(filter(lambda w: len(w) >= min_length, words))
    }


# ============================================================================
# Refactoring-Dokumentation
# ============================================================================

"""
REFACTORING-TECHNIKEN VERWENDET (C1G):

1. Extract Function: Komplexe Logik in separate Funktionen extrahiert
2. Replace Loop with Pipeline: Schleifen durch Map/Filter/Reduce ersetzt
3. Eliminate Mutation: Variablen-Mutation durch immutable Transformationen ersetzt
4. Compose Functions: Kleine Funktionen zu größeren kombiniert
5. Replace Conditional with Polymorphism: If-Statements durch Funktionen-Higher-Order ersetzt

REFACTORING-AUSWIRKUNGEN (C1E):

POSITIV:
- Code ist lesbarer und verständlicher
- Bessere Testbarkeit durch pure functions
- Keine Seiteneffekte = weniger Bugs
- Einfacher zu erweitern und zu warten
- Bessere Wiederverwendbarkeit

RISIKEN (verhindert durch Tests):
- Performance könnte theoretisch schlechter sein (in Praxis meist nicht relevant)
- Längere Funktionsketten könnten schwerer zu debuggen sein
- Team muss funktionale Konzepte verstehen

MASSNAHMEN GEGEN RISIKEN:
- Unit-Tests für alle Funktionen
- Klare Dokumentation
- Schrittweises Refactoring
- Code-Reviews
"""


# ============================================================================
# A1E: Objektorientierte Version (zum Paradigmen-Vergleich)
# ============================================================================

class TextProcessor:
    """
    A1E: Objektorientierte Version der Textverarbeitung
    Zum Vergleich mit prozeduraler und funktionaler Programmierung
    """
    
    def __init__(self, text: str):
        """Initialisiert TextProcessor mit Text - Zustand wird im Objekt gespeichert"""
        self.text = text
        self.words = text.split()
    
    def count_long_words(self, min_length: int) -> int:
        """
        Zählt lange Wörter - verwendet Objektzustand (self.words)
        OO-Charakteristik: Methode arbeitet auf Objektzustand
        """
        count = 0
        for word in self.words:
            if len(word) >= min_length:
                count += 1
        return count
    
    def process(self, min_length: int = 5) -> Dict:
        """
        Verarbeitet Text - verwendet Objektzustand
        OO-Charakteristik: Kann Seiteneffekte haben, arbeitet mit Objektzustand
        """
        return {
            'word_count': len(self.words),
            'longest_word': max(self.words, key=len) if self.words else "",
            'average': sum(len(w) for w in self.words) / len(self.words) if self.words else 0,
            'long_words': [w for w in self.words if len(w) >= min_length]
        }
