def main():
    return {x: {x : True} for x in "string"}


if __name__ == "__main__":
    dict_of_dicts = main()
    print(dict_of_dicts)