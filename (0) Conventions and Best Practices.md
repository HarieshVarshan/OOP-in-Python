# **OOPS CONCEPT CONVENTIONS**

    1. Try to initialize the attributes inside the __init__() constructor.

    2. Naming Convention:
        > CamelCase for classes
        > lower_snake_case for functions and attributes

    3. Keep self as self.
        > Dont do this: (Technically Correct but not preferred)
            - def fancy(rocky,attr):
                rocky.attr = attr

        > Preferred Choice:
            - def fancy(self,attr):
                self.attr = attr

    4. Use DocStrings to Maintain a readability while writing very large codes
        > class Myclass:
            """Does Nothing"""  ==> docstring to explain what the class/ function/ method is doing.
            pass

    5. Class Level Data must be in Capital Letters
        > Don't do this: (Technically correct but not preferred)
            - class Student:
                maximumMarks = 100
                def __init__(self,name,marks):
                    pass

        > Preferred Choice:
            - class Student:
                MAX_MARKS = 100
                def __init__(self,name,marks):
                    pass

    6. Try to keep the same method attribute name to instance attribute name
        >  Don't do this: (Technically correct but not preferred)
            - class Employee:
                def identity(self,id):
                    self.EmployeeID = id  (i.e) Instance Attribute name != Method Attribute name
        > Preferred Choice:
            - class Employee:
                def identity(self,id):
                    self.id = id   (i.e) Instance Attribute name = Method Attribute name

    7. A class can have only one __init__() function.

    8. Python does not have method overloading like C++ and Java.

    9. class ClassName():  is same as class ClassName:
 
