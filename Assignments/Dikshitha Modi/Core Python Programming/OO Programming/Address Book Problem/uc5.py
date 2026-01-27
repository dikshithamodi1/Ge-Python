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

    def delete_contact(self,contact):
        for contact in self.contacts:
            if contact.fname==fname and contact.lname==lname:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
            print("contact not found")

    def show_contacts(self):
        if not self.contacts:
            print("contacts not available")
        for contacts in self.contacts:
            print(contacts)

        
from contact import Contact
from address_book import AddressBook
class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program in AddressBookMain class")

        self.address_book=AddressBook()

        while True:
            print("\n1.add contact")
            print("2.edit contact")
            print("3.remove contact")
            print("4.add multiple contacts")
            print("5.Show contacts")
            print("6.Exit")
            option=input("Enter what action to be performed on address book:")
            if option=="1":
                self.add_contact()
            elif option=="2":
                self.edit_contact()
            elif option=="3":
                self.delete_contact()
            elif option=="4":
                self.add_multiple_contacts()
            elif option=="5":
                self.address_book.show_contacts()
            elif option=="6":
                print("Exsisting address book")
                break
            else:
                print("Invalid choice")

    def add_contact(self):
        fname=input("Enter First Name:")
        lname=input("Enter Last Name:")
        address=input("Enter Address:")
        city=input("Enter city:")
        state=input("Enter State:")
        zip_code=input("Enter Zip Code:")
        phone_no=input("Enter Phone Number:")
        email=input("Enter Email:")

        contact=Contact(fname,lname,address,city,state,zip_code,phone_no,email)
        self.address_book.add_contact(contact)

    def edit_contact(self):
        fname=input("Enter new name to be updated")
        self.address_book.edit_contact(fname)

    def delete_contact(self):
        fname=input("Enter fnmae to delete contact:")
        lname=input("Enter lname to delete contact:")
        self.address_book.delete_contact(fname,lname)

    def add_multiple_contacts(self):
        while True:
            self.add_contact()
            more=input("Add another contact(y/n):")
            if more.lower()!="y":
                break
        
if __name__=="__main__":
    AddressBookMain()
