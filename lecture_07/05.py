count = 0
with open("student.txt", "r") as file:
    for line in file:
        count += 1
print("total lines=", count)
