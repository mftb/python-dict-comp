def dict_inception():
    return {x: {x : True} for x in "string"}


def main():
    dict_of_dicts = dict_inception()
    print(dict_of_dicts)


if __name__ == "__main__":
    main()