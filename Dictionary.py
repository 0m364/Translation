# Dictionary to store language patterns and their translations
translation_patterns = {
    'english': {
        'apple': 'apfel',
        'orange': 'orange',
        'banana': 'banane'
    },
    'german': {
        'apfel': 'apple',
        'orange': 'orange',
        'banane': 'banana'
    }
}

def translate(sentence, source_language, target_language):
    # Check if the source and target languages are available
    if source_language not in translation_patterns or target_language not in translation_patterns:
        return "Language not supported"

    words = sentence.split()
    translated_sentence = []

    for word in words:
        word_lower = word.lower()
        # If the word is found in the dictionary, translate it
        if word_lower in translation_patterns[source_language]:
            translated_sentence.append(translation_patterns[target_language].get(translation_patterns[source_language][word_lower], word))
        else:
            # If the word is not found, keep it as is
            translated_sentence.append(word)

    return ' '.join(translated_sentence)


# Example usage
sentence = "I ate an apple and an orange."
source_language = 'english'
target_language = 'german'

translated_sentence = translate(sentence, source_language, target_language)
print(translated_sentence)
