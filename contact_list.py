class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"Contact '{name}' not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)


if __name__ == "__main__":
    contact_list = ContactList()

    while True:
        print("\n----- Contact List Menu -----")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            contact = Contact(name, phone, email)
            contact_list.add_contact(contact)
            print("Contact added successfully.")
        elif choice == 2:
            name = input("Enter the name of the contact to remove: ")
            contact_list.remove_contact(name)
        elif choice == 3:
            name = input("Enter the name of the contact to search: ")
            contact_list.search_contact(name)
        elif choice == 4:
            print("\n----- Contact List -----")
            contact_list.display_contacts()
        elif choice == 5:
            print("Exiting the Contact List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
