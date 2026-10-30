with open("student.txt", "r") as file:
    lines = file.readlines()
with open("cleaned.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)
print("blank lines removed sucessfully")
