def vowels(word):
    return {letter: True for letter in word if letter in "aeiou"}


def consonants(word):
    return {letter: True for letter in word if letter not in "aeiou"}


def main():
    print(vowels("matheus"))
    print(consonants("matheus"))
    


if __name__ == "__main__":
    main()