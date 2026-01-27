class Employee:
    count=0
    def __init__(self,name):
        self.name=name
        Employee.count+=1
e1 = Employee("Alex")
e2 = Employee("Riya")
print(Employee.count)
