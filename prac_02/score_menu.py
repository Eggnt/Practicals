"""
CP1404/CP5632 - Practical
Program using a menu to determine score status and display stars
"""

MENU = f"(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            category = determine_grade(score)
            print(f"Your score is {category}.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid Choice!\n")
        choice = get_choice()
    print("Goodbye Friend :)")


def get_choice():
    print(MENU)
    choice = input(">>>")
    return choice


def get_valid_score():
    score = int(input("Enter score:"))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100")
        score = int(input("Enter score:\n"))
    return score


def determine_grade(score):
    if score < 0 or score > 100:
        category = "invalid"
    elif score > 90:
        category = "excellent"
    elif score > 50:
        category = "passable"
    else:
        category = "bad"
    return category


def print_stars(score):
    for i in range (0, score):
        print(f"*", sep="", end="")


main()
