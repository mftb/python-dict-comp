def main(a_list, b_list):
    return {x: y for x, y in zip(a_list, b_list)}


if __name__ == "__main__":
    digits = main("1234", [1,2,3,4])
    print(digits)
    for digit in digits:
        assert digits[digit] == int(digit)
        assert str(digits[digit]) == digit