class Circle:
    radius = int(input("enter radius:"))

    def calculate_circum(self):
        circum = 2*3.14*self.radius
        return circum


c1 = Circle()
print("radius:", c1.radius)
print("Circumference:", c1.calculate_circum())
