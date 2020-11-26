class Student:
    MAX_MARKS = 100
    def score(self,lucky):
        print("The marks obtained is ",self.MAX_MARKS)
        print("The lucky number is ",self.lucky)

print(Student.MAX_MARKS , "As a class attribute")
print(Student().MAX_MARKS , "As a instance attribute")
# Student().score(17) # Calling score method without using objects (MAX_MARKS is common to the class but there is no memory allocation for the lucky variable)
# Student.score = classmethod(Student.score) # Converting the score method into a class method
# Student.score(17)  # Calling score method as a class method.
# The above three lines are one and the same