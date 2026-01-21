"""
Functional Utilities - Höherwertige Funktionen, Closures, Funktionen als Objekte
Implementiert B2G, B2F, B2E Kompetenzfelder
"""

from typing import List, Callable, Dict, Any


# ============================================================================
# B2G: Funktionen als Objekte - Funktionen in Variablen speichern
# ============================================================================

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


# ============================================================================
# B2F: Höherwertige Funktionen - Funktionen als Argumente
# ============================================================================

def apply_transformations(text: str, funcs: List[Callable[[str], str]]) -> str:
    """
    B2F: Funktionen als Argumente für andere Funktionen
    Wendet mehrere Transformationen nacheinander an
    """
    result = text
    for func in funcs:
        result = func(result)
    return result


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


def pipe(text: str, *functions: Callable) -> str:
    """
    B2F: Pipeline-Pattern - führt Funktionen sequenziell aus
    """
    return apply_transformations(text, list(functions))


def filter_with_predicate(items: List[str], predicate: Callable[[str], bool]) -> List[str]:
    """
    B2F: Höherwertige Funktion - Filter mit beliebigem Prädikat
    """
    return [item for item in items if predicate(item)]


def map_with_function(items: List[str], func: Callable[[str], Any]) -> List[Any]:
    """
    B2F: Höherwertige Funktion - Map mit beliebiger Transformationsfunktion
    """
    return [func(item) for item in items]


# ============================================================================
# B2E: Closures - Funktionen die Funktionen zurückgeben
# ============================================================================

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


def create_word_filter(min_length: int, max_length: int) -> Callable[[str], List[str]]:
    """
    B2E: Closure - erstellt Filter-Funktion mit gespeicherten Parametern
    """
    def filter_words(text: str) -> List[str]:
        """
        Closure hat Zugriff auf min_length und max_length
        """
        words = text.split()
        return [w for w in words if min_length <= len(w) <= max_length]
    
    return filter_words


def create_counter() -> Callable[[], int]:
    """
    B2E: Closure mit State - Zähler mit gespeichertem Zustand
    """
    count = 0
    
    def increment() -> int:
        nonlocal count
        count += 1
        return count
    
    return increment


def create_text_validator(rules: Dict[str, Any]) -> Callable[[str], bool]:
    """
    B2E: Closure - erstellt Validator mit gespeicherten Regeln
    """
    min_words = rules.get('min_words', 0)
    max_words = rules.get('max_words', float('inf'))
    min_chars = rules.get('min_chars', 0)
    required_words = rules.get('required_words', [])
    
    def validate(text: str) -> bool:
        """
        Closure hat Zugriff auf alle Validierungsregeln
        """
        word_count = len(text.split())
        char_count = len(text)
        
        # Prüfe Wortanzahl
        if not (min_words <= word_count <= max_words):
            return False
        
        # Prüfe Zeichenanzahl
        if char_count < min_chars:
            return False
        
        # Prüfe erforderliche Wörter
        text_lower = text.lower()
        for required_word in required_words:
            if required_word.lower() not in text_lower:
                return False
        
        return True
    
    return validate


def create_transformation_chain(transformations: List[Callable[[str], str]]) -> Callable[[str], str]:
    """
    B2E: Closure - erstellt Transformationskette
    Die Liste von Transformationen wird in der Closure gespeichert
    """
    def transform(text: str) -> str:
        """
        Closure hat Zugriff auf transformations-Liste
        """
        result = text
        for transform_func in transformations:
            result = transform_func(result)
        return result
    
    return transform


# ============================================================================
# Kombinierte höherwertige Funktionen
# ============================================================================

def process_text_with_pipeline(
    text: str,
    validators: List[Callable[[str], bool]],
    transformers: List[Callable[[str], str]],
    filters: List[Callable[[str], bool]]
) -> Dict[str, Any]:
    """
    B2E: Komplexe Anwendung von Closures und höherwertigen Funktionen
    Pipeline mit Validierung, Transformation und Filterung
    """
    result = {
        'original': text,
        'valid': False,
        'transformed': '',
        'filtered_words': []
    }
    
    # Validierung
    is_valid = all(validator(text) for validator in validators)
    result['valid'] = is_valid
    
    if not is_valid:
        return result
    
    # Transformation
    transformed = text
    for transformer in transformers:
        transformed = transformer(transformed)
    result['transformed'] = transformed
    
    # Filterung
    words = transformed.split()
    filtered = [word for word in words 
                if all(filter_func(word) for filter_func in filters)]
    result['filtered_words'] = filtered
    
    return result


