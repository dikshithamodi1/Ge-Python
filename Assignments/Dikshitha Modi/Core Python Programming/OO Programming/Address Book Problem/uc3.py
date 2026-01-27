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

    def edit_contact(self):
        fname=input("Enter new name to be updated")
        self.address_book.edit_contact(fname)

if __name__=="__main__":
    AddressBookMain()


class AddressBook:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):
        self.contacts.append(contact)
        print("contact added to address book")

    def edit_contact(self,contact):
        for contact in self.contacts:
            if contact.fname==fname:
                print("contact found,Enter new details to be updated")

            contact.lname=input("Enter new name to be updated:")
            contact.address=input("Enter new address to be updated:")
            contact.city=input("Enter new city to be updated:")
            contact.state=input("Enter new state to be updated")
            contact.zip_code=input("Enter the new zip code to be updated:")
            contact.phone_no=input("Enter new phone number to be updated:")
            contact.email=input("Enter new email to be updated:")

            print("Contact updated successfully")
            return
        print("Contact not found")
