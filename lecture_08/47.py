class Vehicle:
    def __init__(self, brand, price_per_day):
        self.brand = brand
        self.price_per_day = price_per_day

    def calculate_rent(self, days):
        return self.price_per_day * days


class Car(Vehicle):
    def __init__(self, brand, price_per_day, seats):
        super().__init__(brand, price_per_day)
        self.seats = seats

    def display_details(self, days):
        print("\nCar Details")
        print("Brand:", self.brand)
        print("Seats:", self.seats)
        print("Rental Days:", days)
        print("Total Rent: ₹", self.calculate_rent(days))


class Bike(Vehicle):
    def __init__(self, brand, price_per_day, engine_capacity):
        super().__init__(brand, price_per_day)
        self.engine_capacity = engine_capacity

    def display_details(self, days):
        print("\nBike Details")
        print("Brand:", self.brand)
        print("Engine Capacity:", self.engine_capacity, "CC")
        print("Rental Days:", days)
        print("Total Rent: ₹", self.calculate_rent(days))


# Creating objects
car1 = Car("Toyota", 2000, 5)
bike1 = Bike("Royal Enfield", 800, 350)

# Calculating rental charges
car1.display_details(3)
bike1.display_details(2)
