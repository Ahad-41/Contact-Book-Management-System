def get_valid_name():
    while True:
        name = input("Enter Name: ")
        if not name.isalpha():
            print("Error: The contact's name must only contain letters (no numbers or special characters). Please try again.")
        elif len(name) == 0:
            print("Error: Name cannot be empty. Please provide a valid name.")
        else:
            return name

def get_valid_phone_number():
    while True:
        phone_number = input("Enter Phone Number: ")
        if not phone_number.isdigit():
            print("Error: The phone number must be an integer. Please provide a valid phone number.")
        else:
            return phone_number


def input_contact():
    name = get_valid_name()
    email = input("Enter Email: ")
    phone_number = get_valid_phone_number()
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "address": address
    }

    return contact