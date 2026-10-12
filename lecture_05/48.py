a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))

smaller = min(a, b)

for number in range(smaller, 0, -1):
    if a % number == 0 and b % number == 0:
        print("GCD:", number)
        break
