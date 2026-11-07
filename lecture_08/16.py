class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Balance:", self.balance)


acc1 = BankAccount("Abhi", 500000)
acc1.display_balance()
