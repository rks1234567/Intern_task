class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print("Insufficient Balance")
            return False
        else:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
        
acc1 = BankAccount("abc", 1000)
acc1.deposit(2000)
acc1.withdraw(500)
print(acc1.get_balance())

acc1.withdraw(3000)  
acc1.withdraw(4000)

        

