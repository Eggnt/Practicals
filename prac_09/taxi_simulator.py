from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    user_input = input(MENU).upper()
    while user_input != "Q":
        if user_input == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            current_taxi = get_valid_taxi(max_taxi=len(taxis))
        elif user_input == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_valid_distance()
                taxis[current_taxi].start_fare()
                taxis[current_taxi].drive(distance)
                bill = taxis[current_taxi].get_fare()
                print(f"Your {taxis[current_taxi].name} trip cost you ${bill:.2f}")
                total_bill += bill
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        user_input = input(MENU).upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi(max_taxi):
    try:
        potential_taxi = int(input("Choose taxi: "))
        if 0 <= potential_taxi <= max_taxi:
            return potential_taxi
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")


def get_valid_distance():
    try:
        potential_distance = int(input("Drive how far? "))
        return potential_distance
    except ValueError:
        print("Enter a valid number to drive")


main()
