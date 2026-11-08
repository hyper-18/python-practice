class Car:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, amount):
        self.speed += amount
        print("Speed Increased")

    def decrease_speed(self, amount):
        if amount <= self.speed:
            self.speed -= amount
            print("Speed Decreased")
        else:
            print("Cannot decrease speed")

    def display_speed(self):
        print("Current speed:", self.speed, "km/h")


car1 = Car(50)
car1.display_speed()

car1.increase_speed(30)
car1.display_speed()

car1.decrease_speed(20)
car1.display_speed()
