with open("student.txt", "r") as file:
    content = file.read()

uppercase_count = 0
lowercase_count = 0

for char in content:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("uppercase letters=", uppercase_count)
print("lowercace letters=", lowercase_count)
