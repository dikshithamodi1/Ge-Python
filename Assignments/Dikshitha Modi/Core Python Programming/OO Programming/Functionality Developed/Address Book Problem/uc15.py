class Contact:
    def __init__(self, fname, lname, address, city, state, zip_code, phone_no, email):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_no = phone_no
        self.email = email

    def __str__(self):
        return f"{self.fname}, {self.lname}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone_no}, {self.email}"

    def to_dict(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone_no": self.phone_no,
            "email": self.email
        }


from contact import Contact

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        for c in self.contacts:
            if c.fname == contact.fname and c.lname == contact.lname:
                print("Contact already exists")
                return
        self.contacts.append(contact)
        print("Contact added")

    def edit_contact(self, fname):
        for c in self.contacts:
            if c.fname == fname:
                c.lname = input("Last Name: ")
                c.address = input("Address: ")
                c.city = input("City: ")
                c.state = input("State: ")
                c.zip_code = input("Zip: ")
                c.phone_no = input("Phone: ")
                c.email = input("Email: ")
                print("Contact updated")
                return
        print("Contact not found")

    def delete_contact(self, fname, lname):
        for c in self.contacts:
            if c.fname == fname and c.lname == lname:
                self.contacts.remove(c)
                print("Contact deleted")
                return
        print("Contact not found")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts")
        for c in self.contacts:
            print(c)
