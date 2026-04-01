# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """
    Retorna la cantidad total de letras en el texto.
    Debe USAR las funciones count_vowels y count_consonants.
    """
    cant_total = count_vowels(text) + count_consonants(text)
    return cant_total 

def vowel_percentage(text):

    total = total_letters(text)
    if total == 0:
        return 0.0

    return round((count_vowels(text) / total) * 100, 1)

def analyze_text(text):
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

    Debe USAR las funciones count_vowels, count_consonants, total_letters y vowel_percentage.

    Ejemplo: analyze_text("hola") → "V:2 C:2 T:4 P:50.0%"
    """
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = (vowel_percentage(text))

    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"
