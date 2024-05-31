def dict_inception():
    return {x: {x : True} for x in {str(y): y for y in range(0, 10)}}


def main():
    dict_of_dicts = dict_inception()
    print(dict_of_dicts)


if __name__ == "__main__":
    main()