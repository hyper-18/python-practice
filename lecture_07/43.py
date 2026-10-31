with open("students.txt", "r") as file:
    lines = file.readlines()

highest_marks = -1
top_student = ""

for line in lines:
    parts = line.strip().split(" - ")

    name = parts[0]
    marks = int(parts[1])

    if marks > highest_marks:
        highest_marks = marks
        top_student = name

if top_student:
    print("Top student:", top_student)
    print("Highest marks:", highest_marks)
else:
    print("No student records found.")
