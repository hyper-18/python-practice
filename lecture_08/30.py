class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / 5

    def check_result(self):
        if all(mark >= 35 for mark in self.marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")

    def display_result(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total(), "/ 500")
        print("Percentage:", self.calculate_percentage(), "%")
        self.check_result()


student1 = Student("Abhi", [85, 90, 75, 80, 70])

student1.display_result()
