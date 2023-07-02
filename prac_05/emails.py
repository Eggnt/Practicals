'''Email exercise'''

email_to_name = {}


def main():
    email_address = str(input("Email: "))
    while email_address != "":
        name = convert_email_address_to_name(email_address)
        choice = str(input(f"Is your name {name}? (Y/n) "))
        if choice.upper() != "Y" and choice != "":
            name = str(input("Name: "))
        email_to_name[email_address] = name
        email_address = str(input("Email: "))
    for email_address, name in email_to_name.items():
        print(f"{name} ({email_address})")


def convert_email_address_to_name(email_address):
    potential_name = email_address.split("@")
    potential_name.pop(-1)
    name = ((" ".join(str(potential_name).split("."))).title()).strip("[]'")
    return name


main()
