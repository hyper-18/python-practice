n = int(input("enter a number:"))


def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n-1)


print_reverse(n)
