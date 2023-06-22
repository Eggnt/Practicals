"""
CP1404/CP5632 - Practical
Password checker code
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
REQUIRED_UPPER = 1
REQUIRED_LOWER = 1
REQUIRED_DIGIT = 1
REQUIRED_SPECIAL = 1

def main():
    """Program to get and check a user's password."""
    print(f"Please enter a valid password/\nYour password must be between {MIN_LENGTH} and {MAX_LENGTH} characters,"
          f"and contain:\n    {REQUIRED_UPPER} or more uppercase characters\n    {REQUIRED_LOWER} or more lowercase "
          f"characters\n    {REQUIRED_DIGIT} or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand {REQUIRED_SPECIAL} or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if MIN_LENGTH > len(password) or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        else:
            pass
    if REQUIRED_LOWER > count_lower or REQUIRED_UPPER > count_upper or REQUIRED_DIGIT > count_digit:
        return False

    if SPECIAL_CHARS_REQUIRED:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
        if REQUIRED_SPECIAL > count_special:
            return False
    return True


main()
