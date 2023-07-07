# Dictionary to store language patterns and their translations
translation_patterns = {
    'english': {
        'pattern': ['apple', 'orange', 'banana'],
        'translation': ['apfel', 'orange', 'banane']
    },
    'german': {
        'pattern': ['apfel', 'orange', 'banane'],
        'translation': ['apple', 'orange', 'banana']
    }
}

def translate(sentence, source_language, target_language):
    words = sentence.split()
    translated_sentence = []

    for word in words:
        if word.lower() in translation_patterns[source_language]['pattern']:
            index = translation_patterns[source_language]['pattern'].index(word.lower())
            translated_sentence.append(translation_patterns[target_language]['translation'][index])
        else:
            translated_sentence.append(word)

    return ' '.join(translated_sentence)


# Example usage
sentence = "I ate an apple and an orange."
source_language = 'english'
target_language = 'german'

translated_sentence = translate(sentence, source_language, target_language)
print(translated_sentence)
