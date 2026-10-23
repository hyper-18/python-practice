str = input("enter a word:")


def rev_str(str):
    if len(str) <= 1:
        return str
    return rev_str(str[1:])+str[0]


print(rev_str(str))
