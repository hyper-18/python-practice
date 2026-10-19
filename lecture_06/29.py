a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))


def largest(a, b, c):
    if a > b and a > c:
        print(a, "is largest")
    elif b > a and b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")


largest(a, b, c)
