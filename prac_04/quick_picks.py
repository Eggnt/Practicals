import random


def main():
    all_picks = []
    picks = []
    number_of_picks = int(input("How many quick picks? "))
    get_all_picks(all_picks, number_of_picks, picks)
    print_picks(all_picks)


def print_picks(all_picks):
    for pick in all_picks:
        for position in range(0, 6):
            number = pick[position]
            print(f"{number:2}", end=' ')
        print("")


def get_all_picks(all_picks, number_of_picks, picks):
    for pick in range(0, number_of_picks):
        get_pick(picks)
        all_picks.append(picks)
        picks = []


def get_pick(picks):
    for position in range(0, 6):
        potential_number = random.randint(1, 45)
        while potential_number in picks:
            potential_number = random.randint(0, 45)
        picks.append(potential_number)
        picks.sort()


main()
