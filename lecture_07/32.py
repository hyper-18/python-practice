with open("student.txt", "r") as file:
    content = file.read()
reversed_content = content[::-1]
with open("reversed.txt", "w") as file:
    file.write(reversed_content)
print("file reversed successfully..")
