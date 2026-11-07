class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


p1 = Person("nuh", 14)
p2 = Person("puhman", 19)
p1.display()
p2.display()
