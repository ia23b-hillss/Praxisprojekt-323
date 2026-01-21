# Lernnachweis zu Kompetenzband B1 (B1G, B1F, B1E)

**Kompetenz**: Funktionale Programmierung umsetzen - Algorithmen erklären, zerlegen und implementieren.

## Einleitung

Im Verlauf meines Praxisprojekts habe ich gelernt, wie man Algorithmen in der funktionalen Programmierung konzipiert und umsetzt. Dies war ein wichtiger Schritt, da ich vorher hauptsächlich prozedurale Algorithmen kannte. Die funktionale Herangehensweise erfordert ein anderes Denken: Anstatt Schritt-für-Schritt-Anweisungen zu schreiben, denke ich in Transformationen und Kompositionen von Funktionen. Mein Text Analyzer Projekt bot die perfekte Gelegenheit, diese Konzepte praktisch anzuwenden.

## B1G: Algorithmus erklären

Ein Algorithmus ist eine endliche Folge von Anweisungen zur Lösung eines Problems. In der funktionalen Programmierung bedeutet dies, dass ich einen Algorithmus als eine Komposition von Funktionen betrachte, die Daten transformieren.

In meinem Text Analyzer Projekt habe ich einen Algorithmus zur Textanalyse entwickelt. Dieser Algorithmus nimmt einen Text als Eingabe und liefert verschiedene Statistiken wie Wortanzahl, Zeichenanzahl, Satzanzahl und Durchschnittswortlänge zurück.

**Code-Beispiel B1G - Algorithmus erklären:**

```python
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
```

Dieser Algorithmus zeigt, wie ein komplexes Problem in mehrere einfache Schritte zerlegt wird. Jeder Schritt ist eine reine Funktion, die eine spezifische Berechnung durchführt. Der Algorithmus selbst ist ebenfalls eine reine Funktion, da er nur die Eingabe transformiert und keine Seiteneffekte hat.

Der Vorteil dieser Herangehensweise ist, dass jeder Teil des Algorithmus isoliert getestet werden kann. Wenn ich zum Beispiel die Wortzählung testen möchte, kann ich die Funktion `count_words()` direkt testen, ohne den gesamten Algorithmus ausführen zu müssen.

## B1F: Algorithmen in funktionale Teilstücke aufteilen

Die Zerlegung eines Algorithmus in funktionale Teilstücke ist ein zentrales Konzept der funktionalen Programmierung. Anstatt einen großen, monolithischen Algorithmus zu schreiben, zerlege ich das Problem in kleinere, wiederverwendbare Funktionen.

Mein `analyze_text()` Algorithmus demonstriert dies perfekt: Er besteht aus mehreren kleinen Funktionen, die jeweils eine spezifische Aufgabe erfüllen. `count_words()` zählt Wörter, `count_characters()` zählt Zeichen, `count_sentences()` zählt Sätze, und so weiter.

**Code-Beispiel B1F - Algorithmen zerlegen:**

```python
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

def count_words(text: str) -> int:
    """Pure function - keine Seiteneffekte, deterministisch"""
    if not text.strip():
        return 0
    return len(text.split())

def count_characters(text: str) -> int:
    """Pure function - zählt alle Zeichen im Text"""
    return len(text)

def find_longest_word(text: str) -> str:
    """Pure function - findet das längste Wort"""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
```

Jede dieser Funktionen ist ein funktionales Teilstück, das unabhängig funktioniert und getestet werden kann. Die Zerlegung macht den Code nicht nur verständlicher, sondern auch wartbarer. Wenn ich zum Beispiel die Logik zum Zählen von Sätzen ändern möchte, muss ich nur die Funktion `count_sentences()` anpassen, ohne den Rest des Algorithmus zu beeinflussen.

Die Teilstücke können auch wiederverwendet werden. Die Funktion `count_words()` wird nicht nur in `analyze_text()` verwendet, sondern kann auch in anderen Kontexten genutzt werden, zum Beispiel um die Wortanzahl in einem einzelnen Absatz zu zählen.

## B1E: Funktionen in zusammenhängende Algorithmen implementieren

Die erweiterte Kompetenz zeigt sich darin, wie ich die einzelnen Funktionen zu einem zusammenhängenden Algorithmus kombiniere. Dies erfordert ein Verständnis dafür, wie Funktionen komponiert werden können und wie Daten durch eine Pipeline von Transformationen fließen.

In meinem Projekt habe ich nicht nur einfache Algorithmen implementiert, sondern auch komplexere, die mehrere Transformationen kombinieren. Der `analyze_text()` Algorithmus ist ein gutes Beispiel, aber ich habe auch erweiterte Algorithmen entwickelt, die Map, Filter und Reduce kombinieren.

**Code-Beispiel B1E - Komplexe Algorithmus-Implementierung:**

```python
def analyze_text(text: str) -> Dict:
    """
    Haupt-Algorithmus für Textanalyse
    Kombiniert mehrere funktionale Teilstücke zu einem zusammenhängenden Algorithmus
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

def analyze_word_frequencies(text: str) -> Dict[str, int]:
    """
    Komplexer Algorithmus für Wortfrequenz-Analyse
    Verwendet Map, Filter und Reduce für Datenverarbeitung
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
```

Dieser erweiterte Algorithmus zeigt, wie ich mehrere funktionale Konzepte kombiniere: Map für Transformation, Filter für Selektion und Reduce für Aggregation. Die Funktionen werden zu einer Pipeline zusammengesetzt, durch die die Daten fließen.

Die Implementierung zeigt auch, wie ich Hilfsfunktionen wie `update_freq()` innerhalb des Algorithmus definiere, um die Logik zu kapseln. Dies ist ein wichtiges Konzept in der funktionalen Programmierung: Funktionen können lokal definiert werden, um spezifische Transformationen durchzuführen.

## Lernprozess und Reflexion

Zu Beginn war es schwierig, Algorithmen funktional zu denken. Ich war gewohnt, in Schleifen und Schritt-für-Schritt-Anweisungen zu denken. Die Umstellung auf funktionale Transformationen erforderte eine mentale Verschiebung.

Was mir besonders geholfen hat, war die Zerlegung bestehender prozeduraler Algorithmen in funktionale Teilstücke. Ich habe gelernt, dass jeder Schritt in einem prozeduralen Algorithmus als eine Funktion betrachtet werden kann. Dies half mir, die funktionale Denkweise zu entwickeln.

Die größte Herausforderung war, zu verstehen, wie ich komplexe Algorithmen aus einfachen Funktionen zusammensetzen kann. Besonders die Verwendung von Map, Filter und Reduce war am Anfang verwirrend, aber mit der Zeit wurde es natürlicher. Die Erkenntnis, dass ich Daten durch eine Pipeline von Transformationen schicken kann, anstatt sie Schritt für Schritt zu verarbeiten, war ein wichtiger Durchbruch.

Besonders wertvoll war die Erfahrung, dass funktionale Algorithmen oft kürzer und lesbarer sind als ihre prozeduralen Gegenstücke. Die Deklarativität macht den Code selbsterklärend: Ich beschreibe, was ich will, nicht wie ich es erreiche.

## Zukünftige Schritte

Ich plane, mein Wissen über funktionale Algorithmen weiter zu vertiefen, insbesondere durch die Anwendung in komplexeren Datenverarbeitungsszenarien. Besonders interessiert mich, wie ich funktionale Algorithmen für die Verarbeitung großer Datenmengen optimieren kann und wie ich sie parallelisieren kann.

Ich möchte auch lernen, wie ich funktionale Algorithmen mit anderen Paradigmen kombiniere, um die Vorteile jedes Ansatzes zu nutzen. Die Fähigkeit, Algorithmen funktional zu denken und zu implementieren, wird mir in zukünftigen Projekten sehr nützlich sein, besonders in Bereichen wie Datenanalyse und API-Entwicklung.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher darin, Algorithmen funktional zu konzipieren, zu zerlegen und zu implementieren. Die funktionale Herangehensweise hat meine Fähigkeit, komplexe Probleme zu lösen, erheblich verbessert.


