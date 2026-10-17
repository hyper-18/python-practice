a = int(input("enter a :"))
b = int(input("enter b :"))
operator = (input("enter operator:"))


def calculator(a, b, operator):
    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        if b == 0:
            return "cannot divide by zero"
        print(a/b)
    else:
        return "invalid actions"


calculator(a, b, operator)
