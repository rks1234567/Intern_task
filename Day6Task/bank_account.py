class BankAccount:
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Balance: {self.balance}")