VOWELS = "aeiou"


def vowels(word):
    return {letter: True for letter in word if letter in VOWELS}


def consonants(word):
    return {letter: True for letter in word if letter not in VOWELS}


def main():
    word = "matheus"
    word_vowels = vowels(word)
    word_consonants = consonants(word)
    print(f"{word_vowels=}")
    print("is a in word_vowels?", "a" in word_vowels)
    print("is i in word_vowels?", "i" in word_vowels)
    print("is a a vowel?", word_vowels["a"])
    print(f"{word_consonants=}")
    print("is m in word_consonants?", "m" in word_consonants)
    print("is z in word_consonants?", "z" in word_consonants)
    print("is m a consonant?", word_consonants["m"])


if __name__ == "__main__":
    main()