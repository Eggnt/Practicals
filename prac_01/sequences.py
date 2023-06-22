x_value = int(input("Please enter the first number: "))
y_value = int(input("Please enter the second number: "))
while y_value <= x_value:
    print("Too small!\nThe second number must be larger than the first!")
    y_value = int(input("Please enter the second number: "))
choice = input("i. Show the even numbers from x to y\nii. Show the odd numbers from x to y\niii. Show the squares from x to y"
"\niv. Exit the program\n")
while choice != "iv":
    if choice == "i":
        for i in range(x_value, y_value+1):
            if i % 2 == 0:
                print(i, end=' ')
        print("\n")
    elif choice == "ii":
        for i in range(x_value, y_value+1):
            if i % 2 == 1:
                print(i, end=' ')
        print("\n")
    elif choice == "iii":
        for i in range(x_value, y_value+1):
            print(i*i, end=' ')
        print("\n")
    else:
        print(f"Invalid choice!\n")
    choice = input(
        "i. Show the even numbers from x to y\nii. Show the odd numbers from x to y\niii. Show the squares from x to y"
        "\niv. Exit the program\n")
