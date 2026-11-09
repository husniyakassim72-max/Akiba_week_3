def clean_text(text):
    punctuation = ".,!?;:'\"()"
    for mark in punctuation:
        text = text.replace(mark, "")
    return text.lower()


def count_words(words):
    return len(words)


def count_characters(text):
    return len(text.replace(" ", ""))


def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "aeiou":
            count += 1
    return count


def count_consonants(text):
    count = 0
    for letter in text:
        if letter.isalpha() and letter not in "aeiou":
            count += 1
    return count


def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def word_frequency(words):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def analyze_text(text):
    cleaned = clean_text(text)
    words = cleaned.split()

    frequency = word_frequency(words)

    repeated = []
    for word in frequency:
        if frequency[word] > 1:
            repeated.append(word)

    top_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )[:5]

    print("Words:", count_words(words))
    print("Characters without spaces:", count_characters(cleaned))
    print("Vowels:", count_vowels(cleaned))
    print("Consonants:", count_consonants(cleaned))
    print("Longest word:", longest_word(words))
    print("Word frequency:", frequency)
    print("Repeated words:", repeated)
    print("Top five words:", top_words)


text = "Python is useful and Python is powerful."
analyze_text(text)