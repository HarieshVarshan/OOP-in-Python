class Customer:
    def set_name(self, name):
        self.name = name  # Note: name is local to the method "set_name".

    def identity(self):
        # Note: self.name is an instance variable and only the objects of Customer class can access it.
        print("My name is", self.name)
        # Note: self.name does not belong to Customer class but the objects of this class.


# Ways of Instantiations
# Method 1
Customer.set_name(Customer(), "First")
# Customer.identity(Customer())  # "self.name" is an instance variable and since there are no instances/objects it becomes inaccessible"

# Method 2 (Preferred)
c1 = Customer()
c1.set_name("Second")
c1.identity()

# Method 3
c2 = Customer()
Customer.set_name(c2, "Third")
Customer.identity(c2)

# Method 4
Customer().set_name("Fourth") # Here the function is called but there in no object that is allocated in the memory thus on executing the next line it gives error.
# Customer().identity()   # Causes Error



class MyCounter:
    def set_count(self, count):
        self.count = count

# Understanding the instance variables
mc = MyCounter()
mc.set_count(5)
# The instance/object can modify it's variable/attributes from anywhere in the code.
mc.count = 100
# To avoid this external modifications, In C++ the attributes of an object are written inside the private namespace.
print(mc.count)

