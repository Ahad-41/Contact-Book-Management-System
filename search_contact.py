import input_contact

def search_contact(contact_book):
    target_contact = input_contact.input_contact() 
    for contact in contact_book:
        if (contact == target_contact):
            print(f"Found the contact")
            return

    
    print("Not Fount\n")