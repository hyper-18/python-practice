class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculated_discount(self):
        discount = self.price * 0.10
        final_price = self.price-discount
        return final_price

    def display(self):
        print("Product:", self.name)
        print("Original Price:", self.price)
        print("Discount:10%")
        print("Final Price:", self.calculated_discount())


p1 = Product("Laptop", 95000)
p1.display()
