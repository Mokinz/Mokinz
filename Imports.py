# print("Imported my_module...") - print zqwsze bedzie wywolany nawet jesli importuej tylko funkcje (lol)

test = "Test string"


def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
