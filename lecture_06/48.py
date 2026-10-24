str = input("enter a string:")


def only_digits(str):
    if len(str) == 0:
        return True

    if str[0] < "0" or str[0] > "9":
        return False

    return only_digits(str[1:])


print(only_digits(str))
