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

        

from contact import Contact
from address_book import AddressBook
class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program in AddressBookMain class")

        self.address_book={}
        

        while True:
            print("\n1.create new address book")
            print("2.add contact")
            print("3.edit contact")
            print("4.remove contact")
            print("5.add multiple contacts")
            print("6.Show contacts")
            print("7.Search person by city or state")
            print("8.View persons by city or state")
            print("9.Exit")
            option=input("Enter what action to be performed on address book:")
            book=self.get_address_book()
            if not book:
                continue
            if option=="1":
                self.create_address_book()
            elif option=="2":
                self.add_contact()
            elif option=="3":
                self.edit_contact()
            elif option=="4":
                self.delete_contact()
            elif option=="5":
                self.add_multiple_contacts()
            elif option=="6":
                self.address_book.show_contacts()
            elif option=="7":
                self.search_person_by_city_or_state()
            elif option=="8":
                self.view_persons_by_city_or_state()
            elif option=="9":
                print("Exsisting address book")
                break
            else:
                print("Invalid choice")

    def create_address_book(self):
        name=input("Enter the name of the addres book:")
        if name in self.address_book:
            print("Address book already exsits")
        else:
            self.address_book[name]=AddressBook()
            print("New address book is created")

    def get_address_book(self):
        name=input("Enter address book name:")
        if name not in self.address_book:
            print("Address Book does not exsists")
            create=input("Do you want to create it(y/n)")
            if create.lower()=="y":
                self.address_book[name]=AddressBook()
                print("Address Book created successfully")
        else:
            print("Address book not found")
            return None
        return self.address_book[name]
        
    def add_contact(self):
        book=self.get_address_book()
        if not book:
            return
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
        book=self.get_address_book()
        if not book:
            return
        fname=input("Enter new name to be updated")
        self.address_book.edit_contact(fname)

    def delete_contact(self):
        book=self.get_address_book()
        if not book:
            return
        fname=input("Enter fnmae to delete contact:")
        lname=input("Enter lname to delete contact:")
        self.address_book.delete_contact(fname,lname)

    def add_multiple_contacts(self):
        while True:
            self.add_contact()
            more=input("Add another contact(y/n):")
            if more.lower()!="y":
                break
    #uc8
    def search_person_by_city_or_state(self):
        choice=input("Search by (1) city or (2) state:")
        value=input("Enter name")
        found=False
        for book_name,book in self.address_book:
            for contact in book.contacts:
                if choice=="1" and contact.city==value:
                    print(book_name,"->",contact)
                          found=True
                elif choice=="2" and contact.state==value:
                    print(book_name,"->",contact)
                    found=True
        if not found:
            print("No person found")

    #uc9
    def view_persons_by_city_or_state(self):
        choice=input("View by (1) city or (2) state:")
        results={}
        for book in self.address_book.values():
            for contact in book.contacts:
                key=contact.city if choice == "1" else contact.state:
                    if key not in result:
                        result[key]=[]
                    result[key].append(contact.first_name+ " "+contact.last_name)

        for key,persons in result.items():
            print(key,":",persons)
    def show_contacts(self):
        book=self.get_address_book()
        if not book:
            return
    
if __name__=="__main__":
    AddressBookMain()

