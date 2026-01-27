class Invoice:
    def __init__(self,client_name,amount):
        self.client_name=client_name
        self.amount=amount
    def generate_invoice(self):
        return f"Invoice for {self.client_name} | Amount: {self.amount}"
invo = Invoice("Riya", 5000) 
print(invo.generate_invoice())
