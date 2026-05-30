from bank_account import BankAccount
class SavingsAccount(BankAccount):    
    def __init__(self, account, balance, interest_rate):
        super().__init__(account, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest