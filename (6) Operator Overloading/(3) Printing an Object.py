class Customer:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

cust = Customer("Hariesh",5000)
print(cust)   # <__main__.Customer object at 0x00C47808> (i.e) The user information related to the object is not printed
              # Instead the address location of the object/instance is printed.

# Let's check how an Numpy object is printed
import numpy as np
arr = np.array([1,2,4,5])
print(arr)   # [1,2,4,5]   How does this work?
             # Same like operator overloading but instead of overloading __eq__ (==) , the __str__ or __repr__ (print) is overloaded.