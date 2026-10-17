n = int(input("enter a number:"))


def reverse_num(n):
    reverse = 0
    n = abs(n)
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n//10
    return reverse


print(reverse_num(n))
