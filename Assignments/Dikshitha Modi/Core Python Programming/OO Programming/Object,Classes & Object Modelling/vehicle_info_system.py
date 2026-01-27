class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
v = Vehicle("Tesla", "Model 3")
v.display() 
