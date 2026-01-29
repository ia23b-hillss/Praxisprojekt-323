"""
Flask Text Analyzer Application
Haupt-Applikation für Textanalyse mit funktionaler Programmierung
"""

from flask import Flask, render_template, request, jsonify
from text_analyzer import (
    analyze_text,
    count_words,
    count_characters,
    count_sentences,
    transform_words_map,
    filter_words_by_length,
    calculate_total_word_length_reduce,
    count_long_words_combined,
    analyze_word_frequencies,
    get_top_words,
    sort_words_by_criteria,
    remove_duplicates_sorted,
    filter_words_with_lambda,
    get_simple_lambda_transformations,
    count_long_words_procedural,
    count_long_words_functional,
    process_text_procedural,
    process_text_functional,
    TextProcessor
)
from functional_utils import (
    apply_transformations,
    apply_transformation,
    compose,
    pipe,
    create_text_processor,
    create_word_filter,
    TEXT_TRANSFORMATIONS,
    get_transformation
)

app = Flask(__name__)


@app.route('/')
def index():
    """Hauptseite mit Text-Eingabe"""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    POST-Endpoint für Textanalyse
    Verwendet funktionale Analyse-Funktionen
    """
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # Verwende funktionale Analyse-Funktion
    analysis = analyze_text(text)
    
    # Zusätzliche Analysen mit funktionalen Methoden
    word_frequencies = analyze_word_frequencies(text)
    top_words = get_top_words(text, top_n=5)
    
    return jsonify({
        'success': True,
        'analysis': analysis,
        'word_frequencies': dict(top_words),
        'total_word_length': calculate_total_word_length_reduce(text),
        'long_words_count': count_long_words_combined(text, min_length=5)
    })


@app.route('/transform', methods=['POST'])
def transform():
    """
    POST-Endpoint für Text-Transformationen
    Verwendet höherwertige Funktionen und Funktionen als Objekte
    """
    data = request.get_json()
    text = data.get('text', '')
    transformation_type = data.get('type', 'uppercase')
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # B2G: Funktion als Objekt aus Dictionary holen
    transform_func = get_transformation(transformation_type)
    
    if not transform_func:
        return jsonify({'error': 'Ungültige Transformation'}), 400
    
    # B2F: Funktion als Argument verwenden
    transformed = apply_transformation(text, transform_func)
    
    # Zusätzliche Transformationen mit Map
    words = text.split()
    transformed_words = transform_words_map(text, transform_func)
    
    return jsonify({
        'success': True,
        'original': text,
        'transformed': transformed,
        'transformed_words': transformed_words,
        'transformation_type': transformation_type
    })


@app.route('/transform/advanced', methods=['POST'])
def transform_advanced():
    """
    Erweiterte Transformationen mit Closures und Pipelines
    """
    data = request.get_json()
    text = data.get('text', '')
    config = data.get('config', {})
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # B2E: Verwende Closure-basierte Textprozessor-Factory
    processor = create_text_processor(config)
    processed = processor(text)
    
    # B2F: Verwende Pipeline mit mehreren Funktionen
    pipeline_funcs = [
        str.strip,
        str.lower,
        str.capitalize
    ]
    piped_result = pipe(text, *pipeline_funcs)
    
    # B2F: Verwende Komposition
    composed = compose(str.strip, str.lower, str.title)
    composed_result = composed(text)
    
    return jsonify({
        'success': True,
        'original': text,
        'processed': processed,
        'piped': piped_result,
        'composed': composed_result
    })


@app.route('/filter', methods=['POST'])
def filter_text():
    """
    POST-Endpoint für Text-Filterung
    Verwendet Filter, Lambda-Ausdrücke und funktionale Methoden
    """
    data = request.get_json()
    text = data.get('text', '')
    min_length = data.get('min_length', 0)
    max_length = data.get('max_length', 100)
    remove_duplicates = data.get('remove_duplicates', False)
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # B4G: Filter einzeln anwenden
    filtered_words = filter_words_by_length(text, min_length)
    
    # B3F: Lambda mit mehreren Argumenten (via Closure)
    filtered_by_range = filter_words_with_lambda(text, min_length, max_length)
    
    # B3E: Lambda für Sortierung
    sorted_words = sort_words_by_criteria(text, criteria='length')
    
    # Entferne Duplikate wenn gewünscht
    if remove_duplicates:
        # B3E: Lambda für komplexe Sortierung und Deduplizierung
        unique_words = remove_duplicates_sorted(text)
    else:
        unique_words = text.split()
    
    # B4F: Kombinierte Map, Filter, Reduce
    long_words_total_length = count_long_words_combined(text, min_length)
    
    return jsonify({
        'success': True,
        'original': text,
        'filtered_by_min_length': filtered_words,
        'filtered_by_range': filtered_by_range,
        'sorted_by_length': sorted_words,
        'unique_words': unique_words if remove_duplicates else None,
        'long_words_total_length': long_words_total_length
    })


@app.route('/lambda/demo', methods=['POST'])
def lambda_demo():
    """
    Demo-Endpoint für Lambda-Ausdrücke
    """
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # B3G: Einfache Lambda-Ausdrücke
    lambda_transforms = get_simple_lambda_transformations()
    
    words = text.split()
    results = {}
    
    for name, lambda_func in lambda_transforms.items():
        if name in ['uppercase', 'lowercase']:
            results[name] = lambda_func(text)
        elif name == 'double':
            results[name] = ' '.join([lambda_func(w) for w in words])
        elif name == 'square_length':
            results[name] = [lambda_func(w) for w in words]
    
    # B3E: Lambda für Sortierung
    sorted_by_length = sorted(words, key=lambda w: len(w))
    sorted_by_length_desc = sorted(words, key=lambda w: len(w), reverse=True)
    sorted_alphabetically = sorted(words, key=lambda w: w.lower())
    
    return jsonify({
        'success': True,
        'lambda_transformations': results,
        'sorted_by_length': sorted_by_length,
        'sorted_by_length_desc': sorted_by_length_desc,
        'sorted_alphabetically': sorted_alphabetically
    })


@app.route('/map-filter-reduce/demo', methods=['POST'])
def map_filter_reduce_demo():
    """
    Demo-Endpoint für Map, Filter, Reduce
    Zeigt einzelne und kombinierte Verwendung
    """
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    words = text.split()
    
    # B4G: Map einzeln
    uppercased_words = list(map(str.upper, words))
    word_lengths = list(map(len, words))
    
    # B4G: Filter einzeln
    long_words = list(filter(lambda w: len(w) > 5, words))
    short_words = list(filter(lambda w: len(w) <= 3, words))
    
    # B4G: Reduce einzeln
    total_length = calculate_total_word_length_reduce(text)
    
    # B4F: Kombiniert - Filter -> Map -> Reduce
    long_words_count = count_long_words_combined(text, min_length=5)
    
    # B4E: Komplexe Datenverarbeitung
    frequencies = analyze_word_frequencies(text)
    top_words = get_top_words(text, top_n=10)
    
    return jsonify({
        'success': True,
        'map_results': {
            'uppercased_words': uppercased_words,
            'word_lengths': word_lengths
        },
        'filter_results': {
            'long_words': long_words,
            'short_words': short_words
        },
        'reduce_results': {
            'total_length': total_length
        },
        'combined_results': {
            'long_words_count': long_words_count
        },
        'complex_processing': {
            'word_frequencies': dict(frequencies),
            'top_words': dict(top_words)
        }
    })


@app.route('/refactoring/demo', methods=['POST'])
def refactoring_demo():
    """
    C1G, C1F, C1E: Demonstriert Refactoring von prozedural zu funktional
    Zeigt Unterschiede und Vorteile des Refactorings
    """
    data = request.get_json()
    text = data.get('text', '')
    min_length = data.get('min_length', 5)
    
    if not text.strip():
        return jsonify({'error': 'Bitte geben Sie einen Text ein'}), 400
    
    # Vergleiche prozedural vs. funktional
    procedural_count = count_long_words_procedural(text, min_length)
    functional_count = count_long_words_functional(text, min_length)
    
    procedural_result = process_text_procedural(text, min_length)
    functional_result = process_text_functional(text, min_length)
    
    return jsonify({
        'success': True,
        'text': text,
        'min_length': min_length,
        'count_long_words': {
            'procedural': procedural_count,
            'functional': functional_count,
            'same_result': procedural_count == functional_count
        },
        'process_text': {
            'procedural': procedural_result,
            'functional': functional_result
        },
        'refactoring_benefits': {
            'code_length': {
                'procedural': 'Länger, mehr Zeilen, mehr Variablen',
                'functional': 'Kürzer, deklarativer, weniger Code'
            },
            'mutations': {
                'procedural': 'Verwendet Variablen-Mutation (count += 1)',
                'functional': 'Keine Mutation, immutable Transformationen'
            },
            'testability': {
                'procedural': 'Schwerer zu testen (Seiteneffekte möglich)',
                'functional': 'Einfacher zu testen (pure functions)'
            },
            'readability': {
                'procedural': 'Imperativ, Schritt-für-Schritt',
                'functional': 'Deklarativ, beschreibt WAS nicht WIE'
            }
        }
    })


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
    oo_result = processor.process(min_length)
    
    # Prozedurale Version
    proc_count = count_long_words_procedural(text, min_length)
    proc_result = process_text_procedural(text, min_length)
    
    # Funktionale Version
    func_count = count_long_words_functional(text, min_length)
    func_result = process_text_functional(text, min_length)
    
    return jsonify({
        'success': True,
        'text': text,
        'min_length': min_length,
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
        },
        'all_same_result': (
            oo_count == proc_count == func_count and
            oo_result == proc_result == func_result
        )
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

