class Rectangle:
    length = int(input("enter length:"))
    width = int(input("enter width:"))

    def calculate_area(self):
        area = self.length*self.width
        return area


r1 = Rectangle()
print("length=", r1.length)
print("width=", r1.width)
print("area=", r1.calculate_area())
