class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("invalid deposit amount")
        else:
            self.balance += amount
            print("deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.balance)


account1 = BankAccount("Abhi", 10000)

account1.deposit(2000)
account1.withdraw(3000)
account1.display_balance()
