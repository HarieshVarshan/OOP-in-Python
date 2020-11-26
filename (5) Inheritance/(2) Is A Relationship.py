# Inheritance allows us to make "Is a" Relationship between classes.
# SavingsAccount "is a" BankAccount, possibly with some extra features.
# (i.e) SavingsAccount is a special kind of BankAccount.

# Parent Class
class BankAccount():
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        self.balance-=amount
    
# Child Class 
class SavingsAccount(BankAccount):
    def checkbalance(self):
        print("The available balance is ",self.balance)

savings_acct = SavingsAccount(1000)
print(isinstance(savings_acct,SavingsAccount)) # True
print(isinstance(savings_acct,BankAccount)) # True
bank_acct = BankAccount(5000)
print(isinstance(bank_acct,SavingsAccount)) # False
print(isinstance(bank_acct,BankAccount)) # True