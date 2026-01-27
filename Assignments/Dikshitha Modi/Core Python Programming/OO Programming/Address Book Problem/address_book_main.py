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
            print("9.Count persons by city or state")
            print("10.Sort contacts by name")
            print("11.Sort contacts by city")
            print("12.Sort contacts by state")
            print("13.Sort contacts by Zip")
            print("14.Exit")
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
                self.count_persons_by_city_or_state()
            elif option=="10":
                self.sort_contacts_by_name()
            elif option=="11":
                self.sort_contacts("city")
            elif option=="12":
                self.sort_contacts("state")
            elif option=="13":
                self.sort_contacts("zip")
            elif option=="14":
                self.save_to_file()
            elif option=="15":
                self.load_from_file()
            elif option=="16":
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

    #uc10
    def count_persons_by_city_or_state(self):
        choice=input("Count by (1) city or (2) state:")
        count_map={}
        for book in self.address_book.values():
            for contact in book.contacts:
                key=contact.city if choice =="1" else contact.state
                count_map[key]=count_map.get(key,0)
        for ket,count in count_map.items():
            print(key,":",count)

    #uc11
    def sort_contacts_by_name(self):
        for book_name,book in self.address_book.items():
            print("\nAddress Book:",book_name)
            sorted_contacts=sorted(
                book.contacts,
                key=lambda c:(c.first_name.lower(),c.last_name.lower())
                )
            for contact in sorted_contacts:
                print(contact)
    #uc12
    def sort_contact(seelf,field):
        for book_name,book in self.address_book.items():
            print("\nAddress Book:",book_name)
            if field=="city":
                sorted_contacts=sorted(book.contacts, key=lambda c:city.lower())
            elif field=="state":
                sorted_contacts=sorted(book.contacts, key=lambda c:state.lower())
            elif field=="zip":
                sorted_contacts=sorted(book.contacts, key=lambda c:zip.lower())
            else:
                print("invalid field")
                return
            for contact in sorted_contacts:
                print(contact)

    #uc13
    def  save_to_file(self,filenmae="addressbook.txt"):
        file=open(filename,"w")
        for book_name,book in self.address_book.items():
            print("Address Book:"+book_name+"\n")
            for contact in book.contacts:
                line=f"{contact.fname}, {contact.lname}, {contact.address}"\
                f"{contact.city}, {contact.email}, {contact.zip_code}"
            file.write(line)
        file.close()
        print("Address book saved to file")

    def load_from_file(self,filename="addressbook.txt"):
        file=open(filename,"r")
        current_book=None
        for line in file:
            line=line.strip()
            if line.startswith("AddressBoook"):
                book_name=line.split(":")[1]
                self.address_book(book_name)
                current_book=self.address_book[book_name]
            else:
                data=line.split(",")
                contact=Contact(
                    data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
                current_book.contacts.app(contact)
        file.close()
        print("address book loaded from file")
            
    def show_contacts(self):
        book=self.get_address_book()
        if not book:
            return
    
if __name__=="__main__":
    AddressBookMain()
