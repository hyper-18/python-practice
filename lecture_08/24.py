class MathUtils:

    @staticmethod
    def check_even_odd(number):

        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"


print("10 is:", MathUtils.check_even_odd(10))
print("7 is:", MathUtils.check_even_odd(7))
print("24 is:", MathUtils.check_even_odd(24))
