def main(limit):
    return {[x]: x for x in range(0, limit)}


if __name__ == "__main__":
    digits = main(10)
    print(digits)
    for digit in digits:
        assert digits[digit] == int(digit)
        assert str(digits[digit]) == digit