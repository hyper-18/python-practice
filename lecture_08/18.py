class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5)
        return fahrenheit

    def display(self):
        print("Temperature in Celsius:", self.celsius, "°C")
        print("Temperature in Fahrenheit:",
              self.convert_to_fahrenheit(), "°F")


temp1 = Temperature(37)

temp1.display()
