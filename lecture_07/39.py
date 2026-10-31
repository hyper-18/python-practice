with open("student.txt", "r") as file:
    lines = file.readlines()

lines.sort()

with open("sorted.txt", "w") as file:
    file.writelines(lines)

print("Lines sorted successfully!")
