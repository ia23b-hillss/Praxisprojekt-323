# Lernnachweis zu Kompetenzband B3 (B3G, B3F, B3E)

**Kompetenz**: Funktionale Programmierung umsetzen - Lambda-Ausdrücke für einfache Operationen, mehrere Argumente und Programmfluss-Steuerung.

## Einleitung

Lambda-Ausdrücke waren für mich zunächst ein mysteriöses Konzept, das ich nur aus mathematischen Kontexten kannte. Im Verlauf meines Praxisprojekts habe ich jedoch gelernt, wie mächtig und nützlich Lambda-Ausdrücke in der Programmierung sind. Sie ermöglichen es mir, kleine Funktionen inline zu definieren, ohne eine separate Funktion deklarieren zu müssen. Dies macht den Code kompakter und oft auch lesbarer, besonders wenn ich Funktionen als Argumente übergebe.

## B3G: Einfache Lambda-Ausdrücke

Lambda-Ausdrücke sind anonyme Funktionen, die in einer einzigen Zeile definiert werden können. Sie sind besonders nützlich für einfache Operationen, die nur einmal verwendet werden. In meinem Text Analyzer Projekt habe ich mehrere einfache Lambda-Ausdrücke implementiert.

**Code-Beispiel B3G - Einfache Lambda-Ausdrücke:**

```python
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
```

Diese Lambda-Ausdrücke zeigen einfache Operationen: `lambda x: x.upper()` konvertiert einen String zu Großbuchstaben, `lambda x: x.lower()` zu Kleinbuchstaben, `lambda x: x * 2` verdoppelt einen Wert, und `lambda x: len(x) ** 2` quadriert die Länge eines Strings.

Der Vorteil von Lambda-Ausdrücken ist ihre Kompaktheit. Anstatt eine separate Funktion zu definieren, kann ich die Operation direkt inline schreiben. Dies ist besonders nützlich, wenn ich eine Funktion nur einmal verwende, zum Beispiel als Argument für `map()` oder `filter()`.

In meinem Projekt verwende ich diese Lambda-Ausdrücke für einfache Text-Transformationen. Sie sind leicht zu verstehen und zu verwenden, was sie ideal für einfache Operationen macht.

## B3F: Lambda-Ausdrücke mit mehreren Argumenten

Lambda-Ausdrücke können auch mehrere Argumente verarbeiten. Dies ist besonders nützlich, wenn ich komplexere Transformationen durchführen möchte, die mehrere Parameter benötigen.

In meinem Projekt habe ich Lambda-Ausdrücke implementiert, die mehrere Argumente verwenden, auch wenn dies manchmal über Closures geschieht, die die zusätzlichen Parameter "einfangen".

**Code-Beispiel B3F - Lambda mit mehreren Argumenten:**

```python
def filter_words_with_lambda(text: str, min_length: int, max_length: int) -> List[str]:
    """
    B3F: Lambda mit mehreren Argumenten (via Closure)
    Filtert Wörter nach Längenbereich
    """
    words = text.split()
    # Lambda verwendet min_length und max_length aus Closure
    return list(filter(lambda w: min_length <= len(w) <= max_length, words))
```

Dieses Beispiel zeigt, wie ich Lambda-Ausdrücke mit mehreren Parametern verwende. Der Lambda-Ausdruck `lambda w: min_length <= len(w) <= max_length` verwendet sowohl `min_length` als auch `max_length`, die aus dem äußeren Scope kommen (Closure).

Lambda-Ausdrücke können auch direkt mehrere Argumente haben, zum Beispiel `lambda x, y: x + y` für eine Addition. In meinem Projekt verwende ich dies hauptsächlich in Kombination mit `map()`, wenn ich Transformationen mit mehreren Eingaben durchführen möchte.

Der Vorteil ist, dass ich komplexere Bedingungen und Transformationen inline definieren kann, ohne eine separate Funktion schreiben zu müssen. Dies macht den Code kompakter und oft auch lesbarer, besonders wenn die Logik einfach ist.

## B3E: Lambda-Ausdrücke für Programmfluss-Steuerung

Die erweiterte Anwendung von Lambda-Ausdrücken zeigt sich in der Programmfluss-Steuerung, besonders bei Sortierungen und komplexen Transformationen. Lambda-Ausdrücke können als Schlüsselfunktionen für Sortierungen verwendet werden, um komplexe Sortierkriterien zu definieren.

In meinem Projekt habe ich Lambda-Ausdrücke für verschiedene Sortierungen implementiert, die zeigen, wie mächtig sie für die Programmfluss-Steuerung sind.

**Code-Beispiel B3E - Lambda für Programmfluss:**

```python
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
```

Diese Beispiele zeigen, wie Lambda-Ausdrücke für komplexe Sortierungen verwendet werden können. Der Lambda-Ausdruck `lambda w: (len(w), w)` sortiert zuerst nach Länge und dann alphabetisch, was ein Tupel als Sortierschlüssel verwendet.

Lambda-Ausdrücke für Programmfluss-Steuerung sind besonders mächtig, weil sie es mir ermöglichen, komplexe Kriterien inline zu definieren. Anstatt eine separate Funktion zu schreiben, kann ich die Sortierlogik direkt im `key`-Parameter angeben.

In meinem Projekt verwende ich Lambda-Ausdrücke auch für komplexe Filterungen und Transformationen, die mehrere Bedingungen kombinieren. Dies macht den Code deklarativer: Ich beschreibe, was ich will, nicht wie ich es erreiche.

## Lernprozess und Reflexion

Lambda-Ausdrücke waren für mich zunächst verwirrend. Die Syntax `lambda x: x.upper()` sah seltsam aus, und ich verstand nicht, warum ich sie verwenden sollte, wenn ich auch eine normale Funktion schreiben könnte.

Was mir besonders geholfen hat, war die praktische Anwendung in meinem Projekt. Durch die Verwendung von Lambda-Ausdrücken in `map()`, `filter()` und `sorted()` konnte ich ihre Vorteile direkt erleben. Die Kompaktheit und Lesbarkeit wurden schnell deutlich, besonders bei einfachen Operationen.

Die größte Herausforderung war, zu verstehen, wann ich Lambda-Ausdrücke verwenden sollte und wann eine normale Funktion besser ist. Mit der Zeit lernte ich, dass Lambda-Ausdrücke ideal für einfache, einmalige Operationen sind, während normale Funktionen besser für komplexere Logik oder wiederverwendbare Operationen sind.

Besonders wertvoll war die Erkenntnis, dass Lambda-Ausdrücke den Code deklarativer machen. Anstatt zu beschreiben, wie ich etwas mache, beschreibe ich, was ich will. Dies macht den Code oft lesbarer und wartbarer.

Die Verwendung von Lambda-Ausdrücken für Programmfluss-Steuerung war am Anfang schwierig, besonders bei komplexen Sortierungen. Mit der Zeit wurde es jedoch natürlicher, und ich lernte, wie ich Lambda-Ausdrücke für verschiedene Sortierkriterien verwenden kann.

## Zukünftige Schritte

Ich plane, mein Wissen über Lambda-Ausdrücke weiter zu vertiefen, insbesondere durch die Anwendung in komplexeren Datenverarbeitungsszenarien. Besonders interessiert mich, wie ich Lambda-Ausdrücke für die Verarbeitung von verschachtelten Datenstrukturen verwenden kann.

Ich möchte auch lernen, wann ich Lambda-Ausdrücke verwenden sollte und wann eine normale Funktion besser ist. Die Fähigkeit, Lambda-Ausdrücke effektiv zu verwenden, wird mir in zukünftigen Projekten sehr nützlich sein, besonders in Bereichen wie Datenanalyse und API-Entwicklung.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher im Umgang mit Lambda-Ausdrücken für einfache Operationen, mehrere Argumente und Programmfluss-Steuerung. Lambda-Ausdrücke haben meine Fähigkeit, kompakten und lesbaren Code zu schreiben, erheblich verbessert.


