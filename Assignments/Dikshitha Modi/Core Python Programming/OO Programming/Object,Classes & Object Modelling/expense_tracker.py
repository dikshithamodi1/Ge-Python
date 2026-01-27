class ExpenseTracker:
    def __init__(self):
        self.transactions=[]

    def add_expense(self,amount):
        self.transactions.append(amount)

    def total_expense(self):
        return sum(self.transactions)
    
e = ExpenseTracker() 
e.add_expense(200) 
e.add_expense(300)
print(e.total_expense())
