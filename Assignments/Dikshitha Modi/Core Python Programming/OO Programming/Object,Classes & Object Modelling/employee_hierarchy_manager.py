class Employee:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept

class Manager(Employee):
    def __init__(self,name,dept,team_size):
        super().__init__(name,dept)
        self.name=name
        self.dept=dept
        self.team_size=team_size

    def display(self):
        print(f"Manager: {self.name} | Department: {self.dept} | Team Size: {self.team_size}")
    
m = Manager("Alex", "IT", 10) 
m.display()
