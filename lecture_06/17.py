n = int(input("enter a number:"))


def sum_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        digit = n % 10
        total = total+digit
        n = n//10
    return total


print(sum_digits(n))
