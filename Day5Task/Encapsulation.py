# Encapsulaion
# in encapsulation we can make our attribute private or protected so that data hiding becomes possible.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # now it became private using double underscore
# now if we want to access this private attribute we can use getters and setters method.
    def get_balance(self): # getter
        return self.__balance
    
    def set_balance(self, newBalance):
        self.__balance = newBalance
acc1 = BankAccount("Rohit Sharma", 100000)
acc1.set_balance(200000)
print(acc1.name, acc1.get_balance())
