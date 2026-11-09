class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Abhi", 85)

student1.display()

student1.marks = 95
print("Updated Marks:", student1.marks)

student1.marks = 120
print("Final Marks:", student1.marks)
