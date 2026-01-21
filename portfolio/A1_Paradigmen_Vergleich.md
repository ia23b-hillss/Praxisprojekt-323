# Lernnachweis zu Kompetenzband A1 (A1G, A1F, A1E)

**Kompetenz**: Unterschiede zwischen funktionaler Programmierung und anderen Programmierparadigmen aufzeigen.

## Einleitung

Im Rahmen meines Praxisprojekts, einer Flask-basierten Text-Analyzer-Anwendung, habe ich mich intensiv mit den grundlegenden Konzepten der funktionalen Programmierung auseinandergesetzt. Besonders wichtig war es mir zu verstehen, wie sich funktionale Programmierung von anderen Paradigmen wie der objektorientierten oder prozeduralen Programmierung unterscheidet. Diese Erkenntnisse waren fundamental für die Entwicklung meiner Anwendung, da ich bewusst funktionale Konzepte wie Pure Functions, Immutable Values und Paradigmen-Vergleiche implementiert habe.

## A1G: Eigenschaften von Funktionen beschreiben (Pure Functions)

Eine der ersten wichtigen Erkenntnisse war das Konzept der Pure Functions. Pure Functions sind Funktionen, die keine Seiteneffekte haben und bei gleichen Eingaben immer das gleiche Ergebnis liefern. Sie sind deterministisch und vorhersagbar, was sie besonders wertvoll für Tests und Debugging macht.

In meinem Text Analyzer Projekt habe ich mehrere Pure Functions implementiert. Eine zentrale Funktion ist `count_words()`, die die Anzahl der Wörter in einem Text zählt. Diese Funktion ist ein perfektes Beispiel für eine Pure Function, da sie keine Seiteneffekte hat und immer das gleiche Ergebnis für denselben Input liefert.

**Code-Beispiel A1G - Pure Function:**

```python
def count_words(text: str) -> int:
    """
    Pure function - keine Seiteneffekte, deterministisch
    Zählt die Anzahl Wörter in einem Text.
    """
    if not text.strip():
        return 0
    return len(text.split())
```

Diese Funktion erfüllt alle Kriterien einer Pure Function: Sie hat keine Seiteneffekte, verändert keine globalen Variablen, macht keine I/O-Operationen und ist vollständig deterministisch. Wenn ich diese Funktion mit dem Text "Hallo Welt" aufrufe, erhalte ich immer das Ergebnis 2, unabhängig davon, wie oft oder in welchem Kontext ich sie aufrufe.

Der Unterschied zu einer Prozedur liegt darin, dass eine Prozedur typischerweise Seiteneffekte hat, wie das Drucken auf den Bildschirm, das Schreiben in eine Datei oder das Ändern von globalen Variablen. Eine Pure Function hingegen transformiert nur ihre Eingabe in eine Ausgabe, ohne die Umgebung zu beeinflussen.

## A1F: Immutable Values - Unveränderliche Werte

Ein weiteres wichtiges Konzept der funktionalen Programmierung sind Immutable Values, also unveränderliche Werte. In Python sind Strings bereits immutable, aber das Konzept geht tiefer: Anstatt Variablen zu mutieren, erstellen wir neue Werte durch Transformationen.

In meinem Projekt habe ich mehrere Funktionen implementiert, die dieses Konzept demonstrieren. Die Funktion `uppercase_text()` ist ein gutes Beispiel dafür, wie immutable Transformationen funktionieren.

**Code-Beispiel A1F - Immutable Values:**

```python
def uppercase_text(text: str) -> str:
    """
    Erstellt neuen String statt Mutation - Original bleibt unverändert
    """
    return text.upper()
```

Diese Funktion erstellt einen neuen String, anstatt den ursprünglichen zu verändern. Das bedeutet, dass der Original-Text unverändert bleibt, was besonders wichtig ist, wenn ich später noch auf den ursprünglichen Wert zugreifen möchte. In anderen Programmiersprachen, die mutable Objekte verwenden, könnte eine ähnliche Operation das Original-Objekt verändern, was zu unerwarteten Seiteneffekten führen kann.

Der Vergleich zu referenzierten Objekten in anderen Sprachen zeigt die Vorteile: In Sprachen wie Java oder C# können Objekte mutiert werden, was bedeutet, dass alle Referenzen auf dieses Objekt die Änderungen sehen. In der funktionalen Programmierung vermeiden wir dies, indem wir immer neue Werte erstellen, was die Vorhersagbarkeit und Testbarkeit des Codes erheblich verbessert.

## A1E: Paradigmen-Vergleich - OO, Prozedural und Funktional

Das erweiterte Verständnis zeigt sich im direkten Vergleich der verschiedenen Programmierparadigmen. In meinem Projekt habe ich bewusst dasselbe Problem in drei verschiedenen Paradigmen gelöst, um die Unterschiede deutlich zu machen.

**Code-Beispiel A1E - Paradigmen-Vergleich:**

```python
@app.route('/paradigms/compare', methods=['POST'])
def compare_paradigms():
    """
    A1E: Vergleicht OO, prozedural und funktional
    Zeigt wie dasselbe Problem in verschiedenen Paradigmen gelöst wird
    """
    data = request.get_json()
    text = data.get('text', '')
    min_length = data.get('min_length', 5)
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # OO-Version
    processor = TextProcessor(text)
    oo_count = processor.count_long_words(min_length)
    oo_result = processor.process()
    
    # Prozedurale Version
    proc_count = count_long_words_procedural(text, min_length)
    proc_result = process_text_procedural(text)
    
    # Funktionale Version
    func_count = count_long_words_functional(text, min_length)
    func_result = process_text_functional(text)
    
    return jsonify({
        'success': True,
        'comparison': {
            'object_oriented': {
                'count': oo_count,
                'result': oo_result,
                'characteristics': [
                    'Verwendet Klassen und Objekte',
                    'Zustand wird im Objekt gespeichert (self.words)',
                    'Methoden arbeiten auf Objektzustand',
                    'Kann Seiteneffekte haben',
                    'Kapselung von Daten und Verhalten'
                ]
            },
            'procedural': {
                'count': proc_count,
                'result': proc_result,
                'characteristics': [
                    'Verwendet Funktionen und Variablen',
                    'Mutation von Variablen (count += 1)',
                    'Imperative Kontrollstrukturen (for-Schleifen)',
                    'Schleifen mit if-Bedingungen',
                    'Schritt-für-Schritt Anweisungen'
                ]
            },
            'functional': {
                'count': func_count,
                'result': func_result,
                'characteristics': [
                    'Pure functions ohne Seiteneffekte',
                    'Keine Mutation, immutable Transformationen',
                    'Deklarative Transformationen',
                    'Map/Filter/Reduce statt Schleifen',
                    'Komposition kleiner Funktionen'
                ]
            }
        }
    })
```

Dieser Vergleich zeigt deutlich die unterschiedlichen Ansätze: Die objektorientierte Version verwendet eine Klasse `TextProcessor`, die den Text als Zustand speichert. Die prozedurale Version verwendet Schleifen und mutiert Variablen direkt. Die funktionale Version hingegen verwendet reine Funktionen, Map/Filter/Reduce und immutable Transformationen.

Jedes Paradigma hat seine Stärken: OO ist gut für komplexe Systeme mit vielen Zuständen, prozedural ist einfach und direkt, funktional ist besonders gut für Datenverarbeitung und Parallelisierung. In meinem Projekt habe ich gelernt, wann welches Paradigma am besten geeignet ist.

## Lernprozess und Reflexion

Zu Beginn des Projekts war ich hauptsächlich mit objektorientierter Programmierung vertraut. Die Konzepte der funktionalen Programmierung waren für mich neu und zunächst verwirrend. Besonders das Konzept der Immutability und Pure Functions war am Anfang schwer zu verstehen, da ich gewohnt war, Variablen direkt zu mutieren.

Was mir besonders geholfen hat, war die praktische Anwendung in meinem Text Analyzer Projekt. Durch die Implementierung konkreter Funktionen wie `count_words()` und `uppercase_text()` konnte ich die Konzepte direkt erleben und verstehen. Der Paradigmen-Vergleich war besonders aufschlussreich, da ich sehen konnte, wie dasselbe Problem auf verschiedene Weise gelöst werden kann.

Die größte Herausforderung war, alte Gewohnheiten abzulegen. Ich musste lernen, nicht mehr direkt Variablen zu mutieren, sondern stattdessen neue Werte zu erstellen. Auch das Denken in Transformationen statt in Schleifen war am Anfang ungewohnt, aber mit der Zeit wurde es natürlicher.

Besonders wertvoll war die Erkenntnis, dass funktionale Programmierung nicht nur ein theoretisches Konzept ist, sondern praktische Vorteile bietet: Bessere Testbarkeit, weniger Bugs durch fehlende Seiteneffekte und einfachere Parallelisierung.

## Zukünftige Schritte

Ich plane, mein Wissen über funktionale Programmierung weiter zu vertiefen, insbesondere durch die Anwendung in größeren Projekten. Besonders interessiert mich, wie funktionale Konzepte in der Entwicklung von APIs und Datenverarbeitungspipelines eingesetzt werden können. Ich möchte auch lernen, wann es sinnvoll ist, verschiedene Paradigmen zu kombinieren, um die Vorteile jedes Ansatzes zu nutzen.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher im Umgang mit funktionalen Konzepten und kann bewusst entscheiden, welches Paradigma für welche Aufgabe am besten geeignet ist. Die Fähigkeit, verschiedene Paradigmen zu verstehen und zu vergleichen, wird mir in zukünftigen Projekten sehr nützlich sein.


