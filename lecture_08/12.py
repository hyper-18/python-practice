class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Laptop Brand:", self.brand)
        print("Laptop price:", self.price)


lap1 = Laptop("Asus", 144000)
lap2 = Laptop("lenovo", 200000)
lap1.display()
lap2.display()
