n = int(input("enter a number:"))


def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)


print_numbers(n)
