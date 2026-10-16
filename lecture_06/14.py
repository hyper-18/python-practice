n = int(input("enter n:"))


def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total = total+i
    return total


print(sum_n(n))
