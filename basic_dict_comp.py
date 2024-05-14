def main(a_list):
    return {str(x): x for x in a_list}


if __name__ == "__main__":
    digits = main([1,2,3,4])
    print(digits)
    for digit in digits:
        assert digits[digit] == int(digit)
        assert str(digits[digit]) == digit