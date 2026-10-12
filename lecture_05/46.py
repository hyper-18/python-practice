number = int(input("enter a three digit number:"))
original = number
total = 0
while number > 0:
    digit = number % 10
    total = total+digit**3
    number = number//10
if total == original:
    print("armstrong number")
else:
    print("not a armstrong number")
