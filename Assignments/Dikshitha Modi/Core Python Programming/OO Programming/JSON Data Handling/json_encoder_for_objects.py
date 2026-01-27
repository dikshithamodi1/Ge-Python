import json
from datetime import datetime
class Employee:
    def __init__(self,name,hire_date):
        self.name=name
        self.hire_date=hire_date

class CustomEncoder(json.JSONEncoder):
    def default(self,obj):#if the object is not understandable use this
        if isinstance(obj,Employee):#converts it into the dictionary
            return{
                "name":obj.name,
                "hire_date":obj.hire_date
                }
        if isinstance(obj,datetime):#datetime gets convrted to string as json doesn't support datetimr
            return obj.strftime("%Y-%m-%d")
        return super().default(obj)#asks python to handle this
e = Employee("Alex", datetime(2024, 1, 15))
print(json.dumps(e, cls=CustomEncoder))
        
