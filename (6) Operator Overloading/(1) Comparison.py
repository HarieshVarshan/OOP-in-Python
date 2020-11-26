class Customer:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
customer1 = Customer("Hariesh",50000)
customer2 = Customer("Hariesh",50000)

print(customer1 == customer2)   # False
# Becoz the == operator by default has compared the address locations of customer1 and customer2 which are stored in different locations.

print(customer1)   # <__main__.Customer object at 0x029EF628>
print(customer2)   # <__main__.Customer object at 0x02C97A90>


# Overloaded Operators in NumPy Library
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([1,2,3])
print(array1 == array2)  # [True , True, True]