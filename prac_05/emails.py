'''Email exercise'''

email_to_name = {}


def main():
    email_address = str(input("Email: "))
    name = convert_email_address_to_name(email_address)
    choice = str(input(f"Is your name {name}? (Y/n) "))
    if choice.upper() != "Y" and choice.upper() != "":
        name = str(input("Name: "))
    email_to_name[email_address] = name
    print(email_to_name)


def convert_email_address_to_name(email_address):
    potential_name = email_address.split("@")
    potential_name.pop(-1)
    name = ((" ".join(str(potential_name).split("."))).title()).strip("[]'")
    return name


main()
