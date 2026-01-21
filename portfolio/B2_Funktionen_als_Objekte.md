# Lernnachweis zu Kompetenzband B2 (B2G, B2F, B2E)

**Kompetenz**: Funktionale Programmierung umsetzen - Funktionen als Objekte behandeln, höherwertige Funktionen erstellen und Closures anwenden.

## Einleitung

Eine der faszinierendsten Erkenntnisse in meinem Praxisprojekt war die Erkenntnis, dass Funktionen in Python First-Class Citizens sind. Das bedeutet, dass Funktionen wie normale Objekte behandelt werden können: Sie können in Variablen gespeichert, als Argumente übergeben und von anderen Funktionen zurückgegeben werden. Dies eröffnet völlig neue Möglichkeiten der Programmierung und war fundamental für die Entwicklung meines Text Analyzer Projekts.

## B2G: Funktionen als Objekte behandeln

In Python sind Funktionen Objekte, genau wie Strings, Listen oder andere Datentypen. Das bedeutet, ich kann Funktionen in Variablen speichern, in Listen oder Dictionaries ablegen und sie weitergeben, ohne sie auszuführen.

In meinem Projekt habe ich ein Dictionary erstellt, das verschiedene Text-Transformationen speichert. Jeder Eintrag ist eine Funktion, die ich später verwenden kann.

**Code-Beispiel B2G - Funktionen als Objekte:**

```python
# Funktionen als Objekte in Dictionary speichern
TEXT_TRANSFORMATIONS: Dict[str, Callable[[str], str]] = {
    'uppercase': str.upper,
    'lowercase': str.lower,
    'capitalize': str.capitalize,
    'title': str.title,
    'strip': str.strip
}

# Funktionen in Liste speichern
TRANSFORMATION_PIPELINE: List[Callable[[str], str]] = [
    str.strip,
    str.lower,
    str.capitalize
]

def get_transformation(name: str) -> Callable[[str], str]:
    """
    B2G: Funktion als Objekt zurückgeben
    """
    return TEXT_TRANSFORMATIONS.get(name, lambda x: x)

def apply_transformation(text: str, func: Callable[[str], str]) -> str:
    """
    B2G: Funktion als Objekt verwenden
    """
    return func(text)
```

Dieses Beispiel zeigt, wie ich Funktionen wie normale Objekte behandeln kann. Das Dictionary `TEXT_TRANSFORMATIONS` speichert Funktionen als Werte, und ich kann sie über ihren Schlüssel abrufen. Die Funktion `get_transformation()` gibt eine Funktion zurück, die ich dann später verwenden kann.

Der Unterschied zu anderen Programmiersprachen ist hier besonders deutlich: In Sprachen wie C oder Java müsste ich Interfaces oder Funktionszeiger verwenden, um ähnliches zu erreichen. In Python ist dies direkt und elegant möglich.

## B2F: Höherwertige Funktionen - Funktionen als Argumente

Höherwertige Funktionen sind Funktionen, die andere Funktionen als Argumente nehmen oder Funktionen zurückgeben. Dies ist ein mächtiges Konzept, das es mir ermöglicht, generische Funktionen zu schreiben, die für verschiedene Transformationen verwendet werden können.

In meinem Projekt habe ich mehrere höherwertige Funktionen implementiert, die Funktionen als Argumente nehmen. Die Funktion `compose()` ist ein gutes Beispiel dafür.

**Code-Beispiel B2F - Höherwertige Funktionen:**

```python
def compose(*functions: Callable) -> Callable:
    """
    B2F: Funktionen-Komposition - erstellt neue Funktion aus mehreren
    """
    def composed(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return composed

def apply_transformations(text: str, funcs: List[Callable[[str], str]]) -> str:
    """
    B2F: Funktionen als Argumente für andere Funktionen
    Wendet mehrere Transformationen nacheinander an
    """
    result = text
    for func in funcs:
        result = func(result)
    return result

def pipe(text: str, *functions: Callable) -> str:
    """
    B2F: Pipeline-Pattern - führt Funktionen sequenziell aus
    """
    return apply_transformations(text, list(functions))
```

Die Funktion `compose()` nimmt mehrere Funktionen als Argumente und gibt eine neue Funktion zurück, die alle Transformationen nacheinander anwendet. Dies ist ein klassisches Beispiel für eine höherwertige Funktion: Sie nimmt Funktionen als Input und gibt eine Funktion als Output zurück.

Die Funktion `apply_transformations()` zeigt, wie ich eine Liste von Funktionen als Argument nehmen kann. Dies ermöglicht es mir, verschiedene Transformationen dynamisch anzuwenden, ohne den Code für jede Kombination neu schreiben zu müssen.

Der Vorteil höherwertiger Funktionen ist die Wiederverwendbarkeit und Flexibilität. Ich kann generische Funktionen schreiben, die für verschiedene Zwecke verwendet werden können, indem ich verschiedene Funktionen als Argumente übergebe.

## B2E: Closures - Funktionen die Funktionen zurückgeben

Closures sind ein fortgeschrittenes Konzept, bei dem eine Funktion eine andere Funktion zurückgibt, die Zugriff auf Variablen aus dem äußeren Scope hat. Dies ermöglicht es mir, Funktionen mit "eingebautem" Zustand zu erstellen, ohne globale Variablen zu verwenden.

In meinem Projekt habe ich mehrere Factory-Funktionen implementiert, die Closures verwenden. Die Funktion `create_text_processor()` ist ein gutes Beispiel.

**Code-Beispiel B2E - Closures:**

```python
def create_text_processor(config: Dict[str, Any]) -> Callable[[str], str]:
    """
    B2E: Factory-Funktion mit Closure
    Erstellt einen Textprozessor basierend auf Konfiguration
    Die Konfiguration wird in der Closure gespeichert
    """
    case_mode = config.get('case', 'none')  # 'upper', 'lower', 'none'
    remove_spaces = config.get('remove_spaces', False)
    min_length = config.get('min_length', 0)
    
    def process(text: str) -> str:
        """
        Closure hat Zugriff auf case_mode, remove_spaces, min_length
        """
        result = text
        
        # Wende Case-Transformation an
        if case_mode == 'upper':
            result = result.upper()
        elif case_mode == 'lower':
            result = result.lower()
        
        # Entferne Leerzeichen falls konfiguriert
        if remove_spaces:
            result = result.replace(' ', '')
        
        # Filtere nach Mindestlänge
        words = result.split()
        filtered_words = [w for w in words if len(w) >= min_length]
        result = ' '.join(filtered_words)
        
        return result
    
    return process
```

Diese Funktion zeigt, wie Closures funktionieren: Die innere Funktion `process()` hat Zugriff auf die Variablen `case_mode`, `remove_spaces` und `min_length` aus dem äußeren Scope, auch nachdem `create_text_processor()` bereits zurückgekehrt ist. Dies ermöglicht es mir, eine Funktion mit konfiguriertem Verhalten zu erstellen.

Closures sind besonders nützlich, wenn ich Funktionen mit unterschiedlichen Konfigurationen erstellen möchte, ohne globale Variablen zu verwenden. Jede von `create_text_processor()` zurückgegebene Funktion hat ihren eigenen "eingebauten" Zustand, der durch die Konfiguration bestimmt wird.

In meinem Projekt verwende ich Closures auch für die Erstellung von Filter- und Validierungsfunktionen. Dies macht den Code flexibler und wartbarer, da ich Funktionen mit spezifischem Verhalten erstellen kann, ohne den Code zu duplizieren.

## Lernprozess und Reflexion

Die Konzepte der Funktionen als Objekte und höherwertigen Funktionen waren für mich zunächst abstrakt und schwer zu verstehen. Besonders das Konzept der Closures war verwirrend, da ich nicht verstand, wie eine Funktion auf Variablen zugreifen kann, die außerhalb ihres eigenen Scopes liegen.

Was mir besonders geholfen hat, war die praktische Anwendung in meinem Projekt. Durch die Implementierung von `TEXT_TRANSFORMATIONS` und `create_text_processor()` konnte ich die Konzepte direkt erleben und verstehen. Die Erkenntnis, dass Funktionen einfach Objekte sind, die ich speichern und weitergeben kann, war ein wichtiger Durchbruch.

Die größte Herausforderung war, zu verstehen, wann und wie ich Closures verwenden sollte. Am Anfang war ich unsicher, ob ich Closures oder normale Funktionen mit Parametern verwenden sollte. Mit der Zeit lernte ich, dass Closures besonders nützlich sind, wenn ich Funktionen mit "eingebautem" Zustand erstellen möchte.

Besonders wertvoll war die Erkenntnis, dass höherwertige Funktionen und Closures den Code erheblich flexibler und wiederverwendbarer machen. Die Fähigkeit, Funktionen zu komponieren und zu kombinieren, eröffnet völlig neue Möglichkeiten der Programmierung.

## Zukünftige Schritte

Ich plane, mein Wissen über Funktionen als Objekte und Closures weiter zu vertiefen, insbesondere durch die Anwendung in komplexeren Szenarien. Besonders interessiert mich, wie ich diese Konzepte für die Erstellung von flexiblen APIs und Datenverarbeitungspipelines verwenden kann.

Ich möchte auch lernen, wie ich Closures und höherwertige Funktionen optimal einsetze, um Code-Duplikation zu vermeiden und die Wartbarkeit zu verbessern. Die Fähigkeit, Funktionen als Objekte zu behandeln und Closures zu verwenden, wird mir in zukünftigen Projekten sehr nützlich sein, besonders in Bereichen wie Event-Handling und Konfigurationsmanagement.

Mit den erworbenen Kenntnissen fühle ich mich nun sicher im Umgang mit Funktionen als Objekten, höherwertigen Funktionen und Closures. Diese Konzepte haben meine Fähigkeit, flexiblen und wiederverwendbaren Code zu schreiben, erheblich verbessert.


