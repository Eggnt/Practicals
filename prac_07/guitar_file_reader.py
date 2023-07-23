"""
CP1404 Practical 07
File to read and append guitars
"""

from prac_06.guitar import Guitar



def main():
    guitars = read_file()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_file():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
