# Lernnachweis zu Kompetenzband C1 (C1G, C1F, C1E)

**Kompetenz**: Refactoring und bestehenden Code optimieren - Refactoring-Techniken aufzählen, anwenden und Auswirkungen einschätzen.

## Einleitung

Refactoring war für mich zunächst ein abstraktes Konzept, das ich nur aus theoretischen Kontexten kannte. Im Verlauf meines Praxisprojekts habe ich jedoch gelernt, wie wichtig und wertvoll Refactoring ist. Es ermöglicht es mir, Code zu verbessern, ohne seine Funktionalität zu ändern. Mein Text Analyzer Projekt bot die perfekte Gelegenheit, Refactoring praktisch anzuwenden und die Unterschiede zwischen prozeduraler und funktionaler Programmierung zu erleben.

## C1G: Refactoring-Techniken aufzählen

Refactoring-Techniken sind systematische Methoden, um Code zu verbessern, ohne seine Funktionalität zu ändern. In der funktionalen Programmierung gibt es spezifische Techniken, die darauf abzielen, Code lesbarer, wartbarer und testbarer zu machen.

In meinem Projekt habe ich mehrere Refactoring-Techniken angewendet, um prozeduralen Code in funktionalen Code umzuwandeln.

**Code-Beispiel C1G - Refactoring-Techniken:**

```python
"""
REFACTORING-TECHNIKEN VERWENDET (C1G):

1. Extract Function: Komplexe Logik in separate Funktionen extrahiert
2. Replace Loop with Pipeline: Schleifen durch Map/Filter/Reduce ersetzt
3. Eliminate Mutation: Variablen-Mutation durch immutable Transformationen ersetzt
4. Compose Functions: Kleine Funktionen zu größeren kombiniert
5. Replace Conditional with Polymorphism: If-Statements durch Funktionen-Higher-Order ersetzt
"""
```

Diese Techniken zeigen verschiedene Ansätze zum Refactoring: Extract Function hilft, komplexe Logik zu modularisieren, Replace Loop with Pipeline macht Code deklarativer, Eliminate Mutation reduziert Seiteneffekte, Compose Functions ermöglicht Wiederverwendbarkeit, und Replace Conditional with Polymorphism macht Code flexibler.

In meinem Projekt habe ich diese Techniken verwendet, um prozeduralen Code in funktionalen Code umzuwandeln. Jede Technik hat ihre spezifischen Vorteile und Anwendungsfälle, und das Verständnis dieser Techniken war entscheidend für erfolgreiches Refactoring.

## C1F: Refactoring-Techniken anwenden

Die Anwendung von Refactoring-Techniken erfordert ein tiefes Verständnis davon, wie Code funktioniert und wie er verbessert werden kann. In meinem Projekt habe ich bewusst prozeduralen Code geschrieben und ihn dann in funktionalen Code refactored, um die Unterschiede zu erleben.

**Code-Beispiel C1F - Refactoring anwenden:**

```python
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
        if len(word) > min_length:
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
    """
    words = text.split()
    return reduce(
        lambda acc, w: acc + 1,
        filter(lambda w: len(w) > min_length, words),
        0
    )
```

Dieses Beispiel zeigt den Refactoring-Prozess: Die prozedurale Version verwendet eine Schleife mit Mutation, während die funktionale Version Filter und Reduce verwendet. Der Refactoring-Prozess umfasste mehrere Schritte: Zuerst identifizierte ich die Probleme im prozeduralen Code, dann wandelte ich die Schleife in eine Filter-Operation um, und schließlich verwendete ich Reduce für die Aggregation.

Die Anwendung von Refactoring-Techniken erfordert Sorgfalt und Verständnis. Ich musste sicherstellen, dass das Refactoring das Verhalten des Codes nicht ändert, während ich seine Struktur verbessere. Dies erforderte Tests, um sicherzustellen, dass beide Versionen das gleiche Ergebnis liefern.

## C1E: Refactoring-Auswirkungen einschätzen

Die Einschätzung der Auswirkungen von Refactoring ist entscheidend, um sicherzustellen, dass das Refactoring den Code tatsächlich verbessert und keine unerwünschten Nebeneffekte einführt. In meinem Projekt habe ich die Auswirkungen des Refactorings sorgfältig analysiert.

**Code-Beispiel C1E - Refactoring-Auswirkungen:**

```python
def process_text_procedural(text: str) -> Dict:
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
        if len(word) > 5:
            long_words.append(word)
    result['long_words'] = long_words
    
    return result

def process_text_functional(text: str) -> Dict:
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
        'long_words': list(filter(lambda w: len(w) > 5, words))
    }
```

Dieses Beispiel zeigt die Auswirkungen des Refactorings: Die funktionale Version ist kürzer, lesbarer und wartbarer. Sie verwendet pure functions, was die Testbarkeit verbessert, und sie ist kompositionierbar, was die Wiederverwendbarkeit erhöht.

Die Einschätzung der Auswirkungen umfasste mehrere Aspekte: Lesbarkeit, Wartbarkeit, Testbarkeit, Performance und Erweiterbarkeit. Ich musste sicherstellen, dass das Refactoring den Code in all diesen Aspekten verbessert, ohne unerwünschte Nebeneffekte einzuführen.

Besonders wichtig war die Sicherstellung, dass das Refactoring keine unerwünschten Nebeneffekte hat. Ich habe Tests geschrieben, um sicherzustellen, dass beide Versionen das gleiche Ergebnis liefern, und ich habe die Performance überprüft, um sicherzustellen, dass das Refactoring keine signifikanten Performance-Einbußen verursacht.

## Lernprozess und Reflexion

Refactoring war für mich zunächst ein theoretisches Konzept, das ich nur aus Büchern kannte. Die praktische Anwendung in meinem Projekt war entscheidend für mein Verständnis.

Was mir besonders geholfen hat, war der direkte Vergleich zwischen prozeduralem und funktionalem Code. Durch das Schreiben beider Versionen konnte ich die Unterschiede direkt erleben und verstehen, warum funktionaler Code oft besser ist.

Die größte Herausforderung war, zu verstehen, wann und wie ich Refactoring anwenden sollte. Besonders die Einschätzung der Auswirkungen war schwierig, da ich sicherstellen musste, dass das Refactoring den Code tatsächlich verbessert und keine unerwünschten Nebeneffekte hat.

Besonders wertvoll war die Erkenntnis, dass Refactoring nicht nur Code verbessert, sondern auch das Verständnis des Codes erhöht. Durch das Refactoring lernte ich, wie funktionaler Code funktioniert und warum er oft besser ist als prozeduraler Code.

Die Anwendung von Refactoring-Techniken war am Anfang schwierig, besonders bei komplexen Funktionen. Mit der Zeit wurde es jedoch natürlicher, und ich lernte, wie ich Code systematisch refactoren kann, um ihn zu verbessern.

## Zukünftige Schritte

Ich plane, mein Wissen über Refactoring weiter zu vertiefen, insbesondere durch die Anwendung in größeren Projekten. Besonders interessiert mich, wie ich Refactoring für Legacy-Code verwende und wie ich sicherstelle, dass Refactoring keine unerwünschten Nebeneffekte hat.

Ich möchte auch lernen, wie ich Refactoring-Techniken optimal einsetze, um Code zu verbessern, und wie ich die Auswirkungen von Refactoring systematisch einschätze. Die Fähigkeit, Code zu refactoren und seine Auswirkungen einzuschätzen, wird mir in zukünftigen Projekten sehr nützlich sein, besonders bei der Wartung und Verbesserung bestehender Codebasis.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher im Umgang mit Refactoring-Techniken, ihrer Anwendung und der Einschätzung ihrer Auswirkungen. Refactoring hat meine Fähigkeit, Code zu verbessern und zu warten, erheblich verbessert.


