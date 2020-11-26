# Constructor can help to make the code more readable and easy to maintain, since most of the variables/attributes are initialised within the constructor itself
class Customer:
    # Whenever an instance of Customer class is created the __init__ method is called.
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print("The init method is called!!")


# Advantage of using constructor is that,data can be provided at the time of instantiation itself.
cust = Customer("Hariesh")
print(cust.name, cust.balance)
