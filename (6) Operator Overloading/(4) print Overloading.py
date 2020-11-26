# Two methods to overload print function __str__ or __repr__

# 1) __str__ method
class Customer:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        print("__str__ is called")
        string = """Customer Details:\n\tName: {}\n\tBalance: {}""".format(self.name,self.balance)
        return string
        

customer1 = Customer("Hariesh",3000)
print(customer1)

# 2) __repr__ method  (Preferred)
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        print("__repr__ is called")
        string = "Student('{1}',{0})".format(self.id,self.name)
        return string

s1 = Student("John",20)
print(s1)



# TIPS: To print double quotes use
print("My name is \"Hariesh\".")