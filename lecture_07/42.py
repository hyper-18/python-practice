with open("students.txt", "r") as file:
    lines = file.readlines()

total_marks = 0
count = 0

for line in lines:
    parts = line.strip().split(" - ")
    marks = int(parts[1])

    total_marks += marks
    count += 1

if count > 0:
    average = total_marks / count
    print("Average marks:", average)
else:
    print("No student records found.")
