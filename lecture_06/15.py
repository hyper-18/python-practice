n = int(input("enter n:"))


def multiplication_table(n):
    for i in range(1, 11):
        print(n, "X", i, "=", n*i)


multiplication_table(n)
