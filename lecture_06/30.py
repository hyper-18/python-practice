a = int(input("enter a:"))
b = int(input("enter b:"))
operation = input("enter operator:")


def calculator(a, b, operation):
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        if b == 0:
            print("Cannot divide by zero")
        print(a / b)
    else:
        print("Invalid operation")


calculator(a, b, operation)
