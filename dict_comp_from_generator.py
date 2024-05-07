def main():
    # builds a dictionary with the 10 indo-arabic digits 
    return {str(x): x for x in range(0, 10)}


if __name__ == "__main__":
    digits = main()
    print(digits)
    for digit in digits:
        assert digits[digit] == int(digit)
        assert str(digits[digit]) == digit
    
