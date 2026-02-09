from contact import Contact
from address_book import AddressBook
import csv

class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")

        self.address_book = {}

        while True:
            print("\n1. Create new address book")
            print("2. Add contact")
            print("3. Edit contact")
            print("4. Remove contact")
            print("5. Add multiple contacts")
            print("6. Show contacts")
            print("7. Search person by city/state")
            print("8. View persons by city/state")
            print("9. Count persons by city/state")
            print("10. Sort contacts by name")
            print("11. Sort contacts by city")
            print("12. Sort contacts by state")
            print("13. Sort contacts by zip")
            print("14. Save to CSV")
            print("15. Load from CSV")
            print("16. Exit")

            option = input("Enter choice: ")

            if option == "1":
                self.create_address_book()
            elif option == "2":
                self.add_contact()
            elif option == "3":
                self.edit_contact()
            elif option == "4":
                self.delete_contact()
            elif option == "5":
                self.add_multiple_contacts()
            elif option == "6":
                self.show_contacts()
            elif option == "7":
                self.search_person_by_city_or_state()
            elif option == "8":
                self.view_persons_by_city_or_state()
            elif option == "9":
                self.count_persons_by_city_or_state()
            elif option == "10":
                self.sort_contacts_by_name()
            elif option == "11":
                self.sort_contacts("city")
            elif option == "12":
                self.sort_contacts("state")
            elif option == "13":
                self.sort_contacts("zip_code")
            elif option == "14":
                self.save_to_csv()
            elif option == "15":
                self.load_from_csv()
            elif option == "16":
                print("Exiting Program")
                break
            else:
                print("Invalid choice")

    # ---------------------------------

    def create_address_book(self):
        name = input("Enter address book name: ")
        if name in self.address_book:
            print("Already exists")
        else:
            self.address_book[name] = AddressBook(name)
            print("Address Book Created")

    def get_address_book(self):
        name = input("Enter address book name: ")
        if name not in self.address_book:
            print("Not Found")
            return None
        return self.address_book[name]

    # ---------------------------------

    def add_contact(self):
        book = self.get_address_book()
        if not book:
            return

        contact = Contact(
            input("First Name: "),
            input("Last Name: "),
            input("Address: "),
            input("City: "),
            input("State: "),
            input("Zip: "),
            input("Phone: "),
            input("Email: ")
        )

        book.add_contact(contact)

    def edit_contact(self):
        book = self.get_address_book()
        if not book:
            return

        fname = input("Enter first name to edit: ")
        book.edit_contact(fname)

    def delete_contact(self):
        book = self.get_address_book()
        if not book:
            return

        fname = input("First Name: ")
        lname = input("Last Name: ")
        book.delete_contact(fname, lname)

    def add_multiple_contacts(self):
        while True:
            self.add_contact()
            more = input("Add another? (y/n): ")
            if more.lower() != "y":
                break

    def show_contacts(self):
        book = self.get_address_book()
        if book:
            book.show_contacts()

    # ---------------------------------
    # SEARCH / VIEW / COUNT
    # ---------------------------------

    def search_person_by_city_or_state(self):
        choice = input("1.City  2.State : ")
        value = input("Enter value: ")

        found = False
        for book_name, book in self.address_book.items():
            for contact in book.contacts:
                if choice == "1" and contact.city == value:
                    print(book_name, "->", contact)
                    found = True
                elif choice == "2" and contact.state == value:
                    print(book_name, "->", contact)
                    found = True

        if not found:
            print("No person found")

    def view_persons_by_city_or_state(self):
        choice = input("1.City  2.State : ")
        result = {}

        for book in self.address_book.values():
            for c in book.contacts:
                key = c.city if choice == "1" else c.state
                result.setdefault(key, []).append(c.fname + " " + c.lname)

        for k, v in result.items():
            print(k, ":", v)

    def count_persons_by_city_or_state(self):
        choice = input("1.City  2.State : ")
        count = {}

        for book in self.address_book.values():
            for c in book.contacts:
                key = c.city if choice == "1" else c.state
                count[key] = count.get(key, 0) + 1

        for k, v in count.items():
            print(k, ":", v)

    # ---------------------------------
    # SORTING
    # ---------------------------------

    def sort_contacts_by_name(self):
        for name, book in self.address_book.items():
            print("\nAddress Book:", name)
            for c in sorted(book.contacts, key=lambda x: (x.fname, x.lname)):
                print(c)

    def sort_contacts(self, field):
        for name, book in self.address_book.items():
            print("\nAddress Book:", name)
            for c in sorted(book.contacts, key=lambda x: getattr(x, field)):
                print(c)

    # ---------------------------------
    # CSV FILE
    # ---------------------------------

    def save_to_csv(self):
        filename = "addressbook.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book","FName","LName","Address",
                             "City","State","Zip","Phone","Email"])

            for book_name, book in self.address_book.items():
                for c in book.contacts:
                    writer.writerow([book_name,
                                     c.fname,c.lname,c.address,
                                     c.city,c.state,c.zip_code,
                                     c.phone_no,c.email])
        print("Saved to", filename)

    def load_from_csv(self):
        filename = "addressbook.csv"

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    book_name = row[0]
                    if book_name not in self.address_book:
                        self.address_book[book_name] = AddressBook(book_name)

                    contact = Contact(
                        row[1],row[2],row[3],row[4],
                        row[5],row[6],row[7],row[8]
                    )

                    self.address_book[book_name].contacts.append(contact)

            print("Loaded from", filename)

        except FileNotFoundError:
            print("CSV file not found")

# -------------------------------------

if __name__ == "__main__":
    AddressBookMain()
