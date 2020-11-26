from datetime import datetime
class BetterDate:
    def __init__(self,year,month,day):
        self.year,self.month,self.day = year,month,day
        print("The __init__ method is called")

    @classmethod
    def return_object(cls,date):
        year,month,day = date.year,date.month,date.day
        return cls(year,month,day)

dateobj = datetime.today()
BetterDateObj = BetterDate.return_object(dateobj)
print(BetterDateObj.year,BetterDateObj.month,BetterDateObj.day)


