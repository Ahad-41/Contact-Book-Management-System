# python contact_book.py
import add_contact
import view_all_contacts
import remove_contact
import search_contact
import csv

contact_book = []
with open("all_contacts.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            contact = {
                "name": row[0].strip(),
                "email": row[1].strip(),
                "phone_number": row[2].strip(),
                "address": row[3].strip()
            }
            contact_book.append(contact)
            

while True:
    print("\nWelcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View Contact Book")
    print("3. Remove Contact")
    print("4. Search Contact\n")
    
    menu = int(input("Select Any Valid Option: "))
    
    if menu == 0:
        print("Thank You For Using Contact Book Management System\n")
        exit()
    elif menu == 1:
        contact_book = add_contact.add_contact(contact_book)
    elif menu == 2:
        view_all_contacts.view_all_contacts(contact_book)
    elif menu == 3:
        contact_book = remove_contact.remove_contact(contact_book)
    elif menu == 4:
        search_contact.search_contact(contact_book)
    else:
        print("Pleas Choose a Valid Option!!\n")