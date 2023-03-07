# Когато принтираме банковите акаунти ние искаме да се визуализира името и наличния баланс. В момента не е така.
# Също така получаваме неправилни резултати след извършените операции

import random


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def __str__(self):
        return f"{self.name}: {self.balance:.2f}"


accounts = [
    BankAccount("Alice", 1000),
    BankAccount("Bob", 500),
    BankAccount("Charlie", 2000)
]

for account in accounts:
    amount = random.randint(100, 500)
    print(f"Depositing {amount:.2f} into {account.name}")
    account.deposit(amount)
    print(f"Balance of {account}")


for account in accounts:
    amount = random.randint(100, 1500)
    print(f"Withdrawing {amount:.2f} from {account.name}")
    account.withdraw(amount)
    print(f"Balance of {account}")
