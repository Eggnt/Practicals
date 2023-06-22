"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = int(input("Enter score: "))
    category = determine_grade(score)
    print(f"Your score is {category}.")
    random_score = random.randint(0, 100)
    random_category = determine_grade(random_score)
    print(f"Random score = {random_score}")
    print(f"Your score is {random_category}.")


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


main()
