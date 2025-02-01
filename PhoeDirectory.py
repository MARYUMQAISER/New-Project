class PhoneDirectory:
    def __init__(self):
        self.directory = {}  # Using a dictionary as a hash table

    def add_contact(self, name, phone):
        """Adds a new contact to the directory."""
        self.directory[name] = phone
        print(f"Contact {name} added successfully.")

    def search_contact(self, name):
        """Searches for a contact by name."""
        if name in self.directory:
            print(f"{name}: {self.directory[name]}")
        else:
            print("Contact not found.")

    def update_contact(self, name, new_phone):
        """Updates an existing contact's phone number."""
        if name in self.directory:
            self.directory[name] = new_phone
            print(f"Contact {name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        """Deletes a contact from the directory."""
        if name in self.directory:
            del self.directory[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")

    def display_contacts(self):
        """Displays all contacts in the directory."""
        if self.directory:
            print("Phone Directory:")
            for name, phone in self.directory.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

#  Usage
directory = PhoneDirectory()
directory.add_contact("maryum", "123-893-78223")
directory.add_contact("harram", "367-124-3900")
directory.search_contact("maryum")
directory.update_contact("maryum ", "151-2829-3998")
directory.delete_contact("harram")
directory.display_contacts()
