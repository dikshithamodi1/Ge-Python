class Contact:
    def __init__(self,fname,lname,address,city,state,zip_code,phone_no,email):
        self.fname=fname
        self.lname=lname
        self.address=address
        self.city=city
        self.state=state
        self.zip_code=zip_code
        self.phone_no=phone_no
        self.email=email

    
    def __str__(self):
        return (f"{self.fname}, {self.lname} ,{self.address},{self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")
