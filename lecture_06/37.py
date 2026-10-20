n = int(input("enter a number:"))


def count_digits(n):
    if n == 0:
        return 0
    return 1+count_digits(n//10)


print(count_digits(n))
