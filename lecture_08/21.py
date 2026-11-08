class Student:

    college_name = "MIT"

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("College:", self.college_name)


s1 = Student("nigg", 51)
s2 = Student("nuh", 55)
s3 = Student("puh", 60)
s1.display()
print()
s2.display()
print()
s3.display()
