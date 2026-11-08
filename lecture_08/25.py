class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_average(self):
        average = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Student Name:", self.name)
        print("Average Marks:", average)


student1 = Student("Abhi", 85, 90, 80)

student1.calculate_average()
