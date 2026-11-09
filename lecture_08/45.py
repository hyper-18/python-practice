class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(self.name, "- ₹", self.price)


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(product_name, "removed from cart.")
                return

        print(product_name, "not found.")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def apply_discount(self, discount):
        total = self.calculate_total()
        discounted_total = total - (total * discount / 100)

        return discounted_total

    def display_cart(self):
        if not self.products:
            print("Cart is empty.")
            return

        print("\nShopping Cart:")

        for product in self.products:
            product.display_product()

        print("Total Price: ₹", self.calculate_total())


# Creating products
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)
p3 = Product("Keyboard", 2000)

# Creating shopping cart
cart = ShoppingCart()

# Adding products
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

# Displaying cart
cart.display_cart()

# Applying 10% discount
print("Price after 10% discount: ₹", cart.apply_discount(10))

# Removing a product
cart.remove_product("Mouse")

# Displaying updated cart
cart.display_cart()
