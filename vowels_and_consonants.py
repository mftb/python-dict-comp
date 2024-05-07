def vowels(word):
    return {letter: letter in "aeiou" for letter in word}


def consonants(word):
    return {letter: letter not in "aeiou" for letter in word}


def main():
    print(vowels("matheus"))
    print(consonants("matheus"))
    


if __name__ == "__main__":
    main()