with open("demo.txt", "w") as file:
    file.write("First")

with open("demo.txt", "a") as file:
    file.write(" Second")

with open("demo.txt", "r") as file:
    print(file.read())
