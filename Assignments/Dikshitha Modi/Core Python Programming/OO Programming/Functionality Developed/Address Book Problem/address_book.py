from contact import Contact
import csv

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # -------------------------
    def add_contact(self, contact):
        for existing in self.contacts:
            if existing.fname == contact.fname and existing.lname == contact.lname:
                print("Contact already exists")
                return
        self.contacts.append(contact)
        print("Contact added successfully")

    # -------------------------
    def edit_contact(self, fname):
        for contact in self.contacts:
            if contact.fname == fname:
                print("Contact found, enter new details")

                contact.lname = input("Last Name: ")
                contact.address = input("Address: ")
                contact.city = input("City: ")
                contact.state = input("State: ")
                contact.zip_code = input("Zip Code: ")
                contact.phone_no = input("Phone Number: ")
                contact.email = input("Email: ")

                print("Contact updated successfully")
                return
        print("Contact not found")

    # -------------------------
    def delete_contact(self, fname, lname):
        for contact in self.contacts:
            if contact.fname == fname and contact.lname == lname:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
        print("Contact not found")

    # -------------------------
    def show_contacts(self):
        if not self.contacts:
            print("No contacts available")
            return
        for contact in self.contacts:
            print(contact)

    # =========================
    # CSV FILE OPERATIONS
    # =========================

    def save_to_csv(self):
        filename = self.name + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["FirstName","LastName","Address",
                             "City","State","Zip","Phone","Email"])
            for contact in self.contacts:
                writer.writerow(contact.to_list())
        print("Saved to", filename)

    def load_from_csv(self):
        filename = self.name + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                self.contacts.clear()

                for row in reader:
                    contact = Contact(
                        row[0], row[1], row[2], row[3],
                        row[4], row[5], row[6], row[7]
                    )
                    self.contacts.append(contact)

            print("Loaded from", filename)

        except FileNotFoundError:
            print("CSV file not found")

from contact import Contact
from address_book import AddressBook
import csv
import json

class AddressBookMain:

    def __init__(self):
        self.address_books = {}
        print("Welcome to Address Book")

        while True:
            print("\n1.Create Address Book")
            print("2.Add Contact")
            print("3.Edit Contact")
            print("4.Delete Contact")
            print("5.Show Contacts")
            print("6.Search by City/State")
            print("7.Sort by Name")
            print("8.Save to CSV")
            print("9.Load from CSV")
            print("10.Save to JSON")
            print("11.Load from JSON")
            print("12.Exit")

            ch = input("Enter choice: ")

            if ch == "1":
                self.create_book()
            elif ch == "2":
                self.add_contact()
            elif ch == "3":
                self.edit_contact()
            elif ch == "4":
                self.delete_contact()
            elif ch == "5":
                self.show_contacts()
            elif ch == "6":
                self.search()
            elif ch == "7":
                self.sort_by_name()
            elif ch == "8":
                self.save_csv()
            elif ch == "9":
                self.load_csv()
            elif ch == "10":
                self.save_json()
            elif ch == "11":
                self.load_json()
            elif ch == "12":
                break
            else:
                print("Invalid choice")

    # -----------------------

    def get_book(self):
        name = input("Enter Address Book Name: ")
        if name not in self.address_books:
            print("Not found")
            return None
        return self.address_books[name]

    def create_book(self):
        name = input("Enter Name: ")
        self.address_books[name] = AddressBook(name)
        print("Created")

    def add_contact(self):
        book = self.get_book()
        if not book:
            return
        c = Contact(
            input("First: "),
            input("Last: "),
            input("Address: "),
            input("City: "),
            input("State: "),
            input("Zip: "),
            input("Phone: "),
            input("Email: ")
        )
        book.add_contact(c)

    def edit_contact(self):
        book = self.get_book()
        if book:
            book.edit_contact(input("First name: "))

    def delete_contact(self):
        book = self.get_book()
        if book:
            book.delete_contact(
                input("First name: "),
                input("Last name: ")
            )

    def show_contacts(self):
        book = self.get_book()
        if book:
            book.show_contacts()

    # -----------------------

    def search(self):
        val = input("Enter city or state: ")
        for name, book in self.address_books.items():
            for c in book.contacts:
                if c.city == val or c.state == val:
                    print(name, "->", c)

    def sort_by_name(self):
        for name, book in self.address_books.items():
            print("\n", name)
            for c in sorted(book.contacts, key=lambda x: x.fname):
                print(c)

    # -----------------------
    # CSV
    def save_csv(self):
        with open("addressbook.csv","w",newline="") as f:
            w = csv.writer(f)
            w.writerow(["Book","F","L","Addr","City","State","Zip","Phone","Email"])
            for name, book in self.address_books.items():
                for c in book.contacts:
                    w.writerow([name,c.fname,c.lname,c.address,
                                c.city,c.state,c.zip_code,c.phone_no,c.email])
        print("Saved CSV")

    def load_csv(self):
        try:
            with open("addressbook.csv","r") as f:
                r = csv.reader(f)
                next(r)
                for row in r:
                    name = row[0]
                    if name not in self.address_books:
                        self.address_books[name] = AddressBook(name)
                    c = Contact(row[1],row[2],row[3],row[4],
                                row[5],row[6],row[7],row[8])
                    self.address_books[name].contacts.append(c)
            print("Loaded CSV")
        except:
            print("CSV file missing")

    # -----------------------
    # JSON (UC-15)

    def save_json(self):
        data = {}
        for name, book in self.address_books.items():
            data[name] = []
            for c in book.contacts:
                data[name].append(c.to_dict())

        with open("addressbook.json","w") as f:
            json.dump(data,f,indent=4)

        print("Saved JSON")

    def load_json(self):
        try:
            with open("addressbook.json","r") as f:
                data = json.load(f)
                for name, contacts in data.items():
                    self.address_books[name] = AddressBook(name)
                    for c in contacts:
                        self.address_books[name].contacts.append(
                            Contact(c["fname"],c["lname"],c["address"],
                                    c["city"],c["state"],
                                    c["zip_code"],c["phone_no"],c["email"])
                        )
            print("Loaded JSON")
        except:
            print("JSON file missing")

# -----------------------

if __name__ == "__main__":
    AddressBookMain()
