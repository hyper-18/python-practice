class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_student(self):
        self.display_person()
        print("Roll number:", self.roll_number)


s1 = Student("Nigg", 18, 51)
s1.display_student()
