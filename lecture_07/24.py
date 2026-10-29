with open("student.txt", "r") as file:
    content = file.read()
space_count = 0
for char in content:
    if char == "":
        space_count += 1
print("total spaces:", space_count)
