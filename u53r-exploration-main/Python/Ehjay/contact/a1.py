import os
import json

class ContactList:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        # Load contacts from a file
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        # Save contacts to a file
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone_number):
        # Add a contact to the contact list
        if name in self.contacts:
            print(f"Contact '{name}' already exists. Updating phone number.")
        self.contacts[name] = phone_number
        self.save_contacts()
        print(f"Contact '{name}' added/updated successfully.")

    def remove_contact(self, name):
        # Remove a contact from the contact list
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        # Search for a contact by name
        if name in self.contacts:
            print(f"Contact found: {name} -> {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        # Display all contacts
        print("\n" + "=" * 30)  # Add a separator line for better visibility
        if not self.contacts:
            print("The contact list is empty.")
        else:
            print("Contact List:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")
        print("=" * 30 + "\n")


# Example usage:
contact_list = ContactList()

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        contact_list.add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter contact name to remove: ")
        contact_list.remove_contact(name)
    elif choice == "3":
        name = input("Enter contact name to search: ")
        contact_list.search_contact(name)
    elif choice == "4":
        contact_list.display_contacts()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
