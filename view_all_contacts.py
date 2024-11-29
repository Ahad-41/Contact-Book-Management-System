def view_all_contacts(contact_book):
    if contact_book != []:
        print("-" * 82)
        print(f"{'No':<5} {'Name':<15} {'Email':<30} {'Phone Number':<15} {'Address':<15}")
        print("-" * 82)

        for indx, contact in enumerate(contact_book, start=1):
            print(f"{indx:<5} {contact['name']:<15} {contact['email']:<30} {contact['phone_number']:<15} {contact['address']:<15}")

    else:
        print("Contact Book is Empty\n")