# Class Method is method that belongs to a class.
# Note : Usage of instance attributes are prohibited inside a class method.
# Class methods can be called without the help of instances/objects.

class MyClass:
    def __init__(self):
        print("The __init__ method is called")

    @classmethod  # Class Method decorator to declare a method as class method.
    def decoratedmethod(cls,arg1,arg2):
        cls.arg1 = arg1      # Class Attributes
        cls.arg2 = arg2
        print("The decorated class method is called!!")
    
    def hybridmethod(cls,arg1,arg2): # Error is produced as the first argument is cls.
        cls.arg1 = arg1
        cls.arg2 = arg2
        print("Hybrid method is called!!")

    def normalmethod(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Normal method is called!!")

MyClass.decoratedmethod("Hariesh","Varshan")  # Class Method is called without using objects.
print(MyClass.arg1,MyClass.arg2)   # Class Attributes thus can be called.

MyClass.hybridmethod(MyClass,"John","Timothy")  # Just tested whether this combination works. It produces output but also errors.
print(MyClass.arg1,MyClass.arg2)

MyClass.normalmethod(MyClass(),"Hacker","Friend")
#print(MyClass().arg1.MyClass().arg2)  # The instance variables cannot be accessed without an instance being created.


# Note: ClassName() is equivalent to calling an __init__ function which doesn't mean an object or instance is created.
#       Eventhough the __init__ is called the object is not created (i.e) the ClassName() is not assigned to an object
#       Thus no memory is allocated for storing the instance variable. Hence produces error. That's why instance attributes
#       are not permitted to be used inside a class method.


