n = int(input("enter a number:"))


def count_digits(n):
    count = 0
    n = abs(n)
    if n == 0:
        return 1
    while n > 0:
        n = n//10
        count = count+1
    return count


print(count_digits(n))
