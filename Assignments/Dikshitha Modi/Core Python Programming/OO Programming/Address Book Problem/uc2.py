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

    
class AddressBook:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):
        self.contacts.append(contact)
        print("contact added to address book")

from contact import Contact
from address_book import AddressBook
class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program in AddressBookMain class")

    address_book=AddressBook()

    fname=input("Enter First Name:")
    lname=input("Enter Last Name:")
    address=input("Enter Address:")
    city=input("Enter city:")
    state=input("Enter State:")
    zip_code=input("Enter Zip Code:")
    phone_no=input("Enter Phone Number:")
    email=input("Enter Email:")

    contact=(fname,lname,address,city,state,zip_code,phone_no,email)
    address_book.add_contact(contact)

if __name__=="__main__":
    AddressBookMain()
