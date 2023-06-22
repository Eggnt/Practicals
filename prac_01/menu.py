name = input("Please enter your name: ")
choice = input(f"(H)ello\n(G)oodbye\n(Q)uit\n")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}!")
    elif choice == "G":
        print(f"Goodbye {name}.")
    else:
        print(f"Invalid choice!\n")
    choice = input(f"(H)ello\n(G)oodbye\n(Q)uit\n")
