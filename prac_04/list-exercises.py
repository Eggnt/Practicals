def main():
    number_summary()
    check_username_validity()


def check_username_validity():
    validity = False
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = str(input("Please enter your username: "))
    for name in usernames:
        if username == name:
            print("Access granted")
            validity = True
    if not validity:
        print("Access denied")


def number_summary():
    numbers = []
    for entry in range(0, 5):
        numbers.append(int(input(f"Please enter number {entry + 1}: ")))
    print(f"The first number is {numbers[0]}\nThe last number is {numbers[-1]}\n"
          f"The smallest number is {min(numbers)}\nThe largest number is {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers) / 5}")


main()
