with open("student.txt", "r") as source:
    content = source.read()
with open("backup.txt", "w") as destination:
    destination.write(content)
print("file copied successfully")
