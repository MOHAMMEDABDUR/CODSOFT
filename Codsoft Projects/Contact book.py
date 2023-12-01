contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"{name} has been added to your contacts.")

def view_contact_list():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name}: {details['Phone']}")
        print("--------------------")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = []
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["Phone"]:
            found_contacts.append((name, details["Phone"]))

    if found_contacts:
        print("\nSearch Results:")
        for name, phone in found_contacts:
            print(f"{name}: {phone}")
        print("--------------------")
    else:
        print("Contact not found.")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    if name_to_update in contacts:
        print("\nCurrent details:")
        print(f"Phone: {contacts[name_to_update]['Phone']}")
        print(f"Email: {contacts[name_to_update]['Email']}")
        print(f"Address: {contacts[name_to_update]['Address']}")
        
        contacts[name_to_update]["Phone"] = input("Enter the new phone number: ")
        contacts[name_to_update]["Email"] = input("Enter the new email: ")
        contacts[name_to_update]["Address"] = input("Enter the new address: ")

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"{name_to_delete} has been deleted from your contacts.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__== "_main_":
    main()