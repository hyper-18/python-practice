class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "cannot divide by 0"
        return a / b


calc = Calculator()
num1 = int(input("enter a number:"))
num2 = int(input("enter number:"))

print("Addition:", calc.add(num1, num2))
print("Subtraction:", calc.sub(num1, num2))
print("Multiplication:", calc.mult(num1, num2))
print("Division:", calc.div(num1, num2))
