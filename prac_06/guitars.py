from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = str(input("Name: "))
    print("\n... snip ...\n\nThese are my guitars:")
    max_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
