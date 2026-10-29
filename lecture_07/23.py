with open("student.txt", "r") as file:
    content = file.read()
digit_count = 0
for char in content:
    if char.isdigit():
        digit_count += 1
print("total digits=", digit_count)
