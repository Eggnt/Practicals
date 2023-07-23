"""
CP1404 Practical 07
File to read and append guitars
"""

from prac_06.guitar import Guitar


def main():
    guitars = read_file()
    get_new_guitars(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


def get_new_guitars(guitars):
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = str(input("Name: "))
    return guitars


def read_file():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
