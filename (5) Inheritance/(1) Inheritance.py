# Parent Class
class BankAccount():
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        self.balance-=amount
    
# Child Class (Has access to all the instance methods and attributes of Parent Class)
class SavingsAccount(BankAccount):
    def checkbalance(self):
        print("The available balance is ",self.balance)

savings_acct = SavingsAccount(50000)   # savings_acct.balance = 50000
print(type(savings_acct))
savings_acct.withdraw(5000)    # savings_acct.amount = 5000     savings_acct.balance = 45000
savings_acct.checkbalance()    # savings_acct.balance = 45000
