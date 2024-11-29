import save_all_contacts
import input_contact

def add_contact(contact_book):
    inputContact = input_contact.input_contact()

    if any(contact["phone_number"] == inputContact["phone_number"] for contact in contact_book):
        print("Error: A contact with this phone number already exists. Contact not added.")
        return contact_book

    contact_book.append(inputContact)
    save_all_contacts.save_all_contacts(contact_book)
    print("Contact Added Successully\n")
    
    return contact_book
    