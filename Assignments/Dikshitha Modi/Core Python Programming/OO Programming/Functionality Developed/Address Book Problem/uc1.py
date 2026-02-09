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

    
from contact import Contact
class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program in AddressBookMain class")

    contact=Contact("Dikshitha","Modi","somajiguda ranigung maqta","Hyderabad","Telangana","500001","8328457118","dikshithaexample@gmail.com")
    print("Contact Created Successfully")

if __name__=="__main__":
    address=AddressBookMain()
