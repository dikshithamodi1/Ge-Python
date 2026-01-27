class Product:
    def __init__(self,name,stock):
        self.name=name
        self.stock=stock
    def add_stock(self,quantity):
        self.stock+=quantity
    def sell(self,quantity):
        if quantity<=self.stock:
            self.stock+=quantity
        else:
            print("Not enough stock")
p=Product("Laptop",5)
p.sell(2)
print(p.stock)
