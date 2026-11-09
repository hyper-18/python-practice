class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def view_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


account1 = BankAccount("Abhi", 10000)

account1.deposit(2000)
account1.withdraw(3000)
account1.view_balance()
