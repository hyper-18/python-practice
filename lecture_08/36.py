class Shape:
    def display(self):
        print("Calculating shape area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


c1 = Circle(5)
r1 = Rectangle(10, 5)
c1.display()
print("Circle Area:", c1.area())
r1.display()
print("Rectangle Area:", r1.area())
