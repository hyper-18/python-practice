n = int(input("enter a palindrome number:"))


def is_palindrome(n):
    original = n
    reverse = 0
    n = abs(n)
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n//10
    if original >= 0 and original == reverse:
        return True
    else:
        return False


print(is_palindrome(n))
