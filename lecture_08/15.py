class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 80:
            return "B"

        elif self.marks >= 70:
            return "C"

        elif self.marks >= 60:
            return "D"

        else:
            return "F"

    def display(self):
        print("Student name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


student1 = Student("Abhi", 95)
student2 = Student("Rahul", 92)
student3 = Student("Priya", 55)

student1.display()

student2.display()

student3.display()
