import json
import os


# Student Class
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("----------------------")

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks
        }


# Student Management Class
class StudentManagement:

    def __init__(self):
        self.students = []
        self.filename = "students.json"
        self.load_data()

    # Load records from file
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                self.students = [
                    Student(item["roll_no"], item["name"], item["marks"])
                    for item in data
                ]

            except (json.JSONDecodeError, KeyError, TypeError):
                print("Error: Student file contains invalid data.")

    # Save records to file
    def save_data(self):
        data = [student.to_dict() for student in self.students]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add student
    def add_student(self):
        roll_no = input("Enter Roll Number: ").strip()

        if any(s.roll_no == roll_no for s in self.students):
            print("Roll number already exists.")
            return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        try:
            marks = float(input("Enter Marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Please enter valid numeric marks.")
            return

        student = Student(roll_no, name, marks)

        self.students.append(student)
        self.save_data()

        print("Student added successfully.")

    # View all students
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n===== STUDENT RECORDS =====")

        for student in self.students:
            student.display()

    # Search student
    def search_student(self):
        roll_no = input("Enter Roll Number to Search: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display()
                return

        print("Student not found.")

    # Update marks
    def update_student(self):
        roll_no = input("Enter Roll Number to Update: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:

                try:
                    marks = float(input("Enter New Marks: "))

                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return

                except ValueError:
                    print("Invalid marks.")
                    return

                student.marks = marks
                self.save_data()

                print("Student marks updated successfully.")
                return

        print("Student not found.")

    # Delete student
    def delete_student(self):
        roll_no = input("Enter Roll Number to Delete: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.save_data()

                print("Student deleted successfully.")
                return

        print("Student not found.")

    # Main menu
    def menu(self):

        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Try again.")


# Creating application object
app = StudentManagement()

# Starting application
app.menu()
