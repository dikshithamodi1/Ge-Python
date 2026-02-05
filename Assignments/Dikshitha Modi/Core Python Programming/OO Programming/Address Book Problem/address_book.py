from contact import Contact
class AddressBook:
    def __init__(self,name):
        self.name=name
        self.contacts=[]

    def add_contact(self,contact):
        for exsisting in self.contacts:
            if(exsisting.fname==contact.fname and exsisting.lname==contact.lname):
                print("contact already exsits")
                return
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

        
