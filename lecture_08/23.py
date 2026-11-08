class Employee:

    company_name = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    def display(self):
        print("Employee:", self.name)
        print("Salary: ₹", self.salary)
        print("Company:", self.company_name)


emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 60000)

print("--- Before Changing Company ---")
emp1.display()
print()
emp2.display()

Employee.change_company("Microsoft")

print("\n--- After Changing Company ---")
emp1.display()
print()
emp2.display()
