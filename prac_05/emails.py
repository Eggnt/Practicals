'''Email exercise'''

email_to_name = {}


def main():
    email_address = str(input("Email: "))
    name = get_name(email_address)
    print(email_to_name)


def get_name(email_address):
    potential_name = email_address.split("@")
    potential_name.pop(-1)
    name = ((" ".join(str(potential_name).split("."))).title()).strip("[]'")
    choice = str(input(f"Is your name {name}? (Y/n) "))
    if choice.upper() != "Y" and choice.upper() != "":
        name = str(input("Name: "))
    email_to_name[email_address] = name
    return name


main()
