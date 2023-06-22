def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Please enter a password with at least 10 characters: ")
    while len(password) < 10:
        password = input("Please enter a password with at least 10 characters: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
