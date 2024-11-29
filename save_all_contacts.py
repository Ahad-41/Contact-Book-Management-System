def save_all_contacts(contact_book):
    with open("all_contacts.csv", "w") as file:
        for contact in contact_book:
            file.write(f"{contact['name']}, {contact['email']}, {contact['phone_number']}, {contact['address']}\n")