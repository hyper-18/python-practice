with open("student.txt", "r") as file:
    lines = file.readlines()

with open("numbered.txt", "w") as file:
    for number, line in enumerate(lines, start=1):
        file.write(f"{number}. {line}")

print("Line numbers added successfully!")
