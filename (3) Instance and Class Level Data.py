# Instance Level Data / Instance Attributes
print("Instance Level Data")
class Employee:
    def __init__(self,name,salary): # name , salary attributes are local to the method/constructor and cannot be used outside of it.
        self.name = name            # self.name,self.salary can be accessed only by the instances of the class.
        self.salary = salary        # Thus, self.name, self.salary are Instance Level Data.

emp1 = Employee("Hariesh",1200)
emp2 = Employee("John",1300)
print(emp1.name,emp2.salary)  # Valid commands
# print(Employee.salary)  # This throws an error since the Employee class does not have class attribute called 'salary'

# Class Level Data / Class Attributes
print("Class Level Data")
class Student:
    MAX_MARKS = 100    # class level data (Common to all the instances of the student class)
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1 = Student("Hariesh",99) 
s2 = Student("John",100)
print(s1.MAX_MARKS,s2.MAX_MARKS,Student.MAX_MARKS)   # The instances s1, s2 can also access and also the class can also access


        
        