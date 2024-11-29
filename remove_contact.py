import input_contact
import save_all_contacts

def remove_contact(contact_book):
    target_contact = input_contact.input_contact() 

    initial_length = len(contact_book)
    contact_book = [contact for contact in contact_book if contact != target_contact]
    
    if len(contact_book) < initial_length:
        save_all_contacts.save_all_contacts(contact_book)
        print("Contact Reemoved Successfully.\n")
    else:
        print("No Contact Found With This Phone Number.\n")
    
    return contact_book
    