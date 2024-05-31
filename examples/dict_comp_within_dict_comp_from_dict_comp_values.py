def dict_inception():
    my_dict = {str(y): y for y in range(0, 10)}
    return {x: {x : True} for x in my_dict.values()}


def main():
    dict_of_dicts = dict_inception()
    print(dict_of_dicts)


if __name__ == "__main__":
    main()