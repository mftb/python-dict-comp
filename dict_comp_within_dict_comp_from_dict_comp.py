def main():
    return {x: {x : True} for x in {str(y): y for y in range(0, 10)}}


if __name__ == "__main__":
    dict_of_dicts = main()
    print(dict_of_dicts)