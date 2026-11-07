class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 0.15
        return bonus

    def calculate_total_salary(self):
        total = self.salary + self.calculate_bonus()
        return total

    def display(self):
        print("Employee Name:", self.name)
        print("Original Salary: ₹", self.salary)
        print("Bonus: ₹", self.calculate_bonus())
        print("Total Salary: ₹", self.calculate_total_salary())


emp1 = Employee("Abhi", 40000)

emp1.display()
