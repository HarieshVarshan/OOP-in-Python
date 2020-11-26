# Parent Class
class BankAccount():
    def __init__(self,balance):
        self.balance = balance
        print("Parent Constructor is called")

    def withdraw(self,amount):
        self.balance-=amount
    
# Child Class 
class SavingsAccount(BankAccount):
    def __init__(self,balance,interest_rate):    # Constructor for Savings Account
        BankAccount.__init__(self,balance)       # Parent Constuctor is manually called
        self.interest_rate = interest_rate
        print("Child Constructor is called")
       
    def checkbalance(self):
        print("The available balance is ",self.balance)

savings_acct = SavingsAccount(45000,0.3)


