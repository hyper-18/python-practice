with open("student.txt", "r") as file:
    lines = file.readlines()

unique_lines = []

for line in lines:
    if line not in unique_lines:
        unique_lines.append(line)

with open("unique.txt", "w") as file:
    file.writelines(unique_lines)

print("Duplicate lines removed successfully!")
