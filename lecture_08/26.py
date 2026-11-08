class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Updated Balance:", self.balance)


account1 = BankAccount("Abhi", 5000)

account1.deposit(2000)
