from datetime import date

expense_name = input("Enter expense name: ")
amount = float(input("Enter expense amount: "))

today = date.today()

with open("expenses.txt", "a") as file:
    file.write(f"{today} - {expense_name} - ₹{amount:.2f}\n")

print("Expense saved successfully!")
