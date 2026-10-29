with open("student.txt", "r") as file:
    content = file.read()

uppercase_content = content.upper()

with open("student.txt", "w") as file:
    file.write(uppercase_content)

print("File converted to uppercase!")
