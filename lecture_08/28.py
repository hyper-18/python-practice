class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item, "removed from cart.")
        else:
            print(item, "not found in cart.")

    def display_items(self):
        if len(self.items) == 0:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print("-", item)


cart1 = ShoppingCart()

cart1.add_item("Laptop")
cart1.add_item("Mouse")
cart1.add_item("Keyboard")

cart1.display_items()

cart1.remove_item("Mouse")

cart1.display_items()
