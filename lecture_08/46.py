class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        print("Available Balance: ₹", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print("₹", amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")


# Creating ATM object
atm = ATM(1234, 10000)

# PIN verification
entered_pin = int(input("Enter your ATM PIN: "))

if atm.verify_pin(entered_pin):

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")
