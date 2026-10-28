with open("student.txt", "r") as file:
    content = file.read()

vovels = "aeiouAEIOU"
count = 0

for char in content:
    if char in vovels:
        count += 1
print("Total vovels=", count)
