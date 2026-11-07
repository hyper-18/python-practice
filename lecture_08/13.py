class Mobile:
    def __init__(self, brand, model, price, battery):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = battery

    def display(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Model:", self.model)
        print("Mobile Price:", self.price)
        print("Mobile Battery:", self.battery)


mob1 = Mobile("Samsung", "s24", 45000, "4500mAh")
mob2 = Mobile("OPPO", "Reno 10", 60000, "5000mAH")
mob1.display()
mob2.display()
