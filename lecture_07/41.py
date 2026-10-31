with open("students.txt", "w") as file:
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")

        file.write(name + " - " + marks + "\n")

print("Student records saved successfully!")
