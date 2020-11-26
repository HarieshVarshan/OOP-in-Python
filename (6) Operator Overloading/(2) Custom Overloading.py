class Student():
    def __init__(self,name,id):
        self.id, self.name = id,name
    
    def __eq__(self, other):    # __eq__ will be called when == is used.
        print("__eq__ is called")
        return (self.name == other.name) and (self.id == other.id)

s1 = Student("John",20)
s2 = Student("John",20)
print(s1 == s2)
s1.name = "Hariesh"
print(s1 == s2)



# Other Comparison Operators
#   OPERATOR                 METHOD 
#      ==                   __eq__()
#      !=                   __ne__()
#      >=                   __ge__()
#      <=                   __le__()
#      >                    __gt__()
#      <                    __lt__() 


