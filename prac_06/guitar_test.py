from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013)


def main():
    test(gibson, 101, True)
    test(another, 10, False)


def test(guitar, expected_age, expected_vintage):
    print(f"{guitar.name} get_age() - Expected {expected_age}. Got {guitar.get_age()}"
          f"\n{guitar.name} is_vintage() - Expected {expected_vintage} got {guitar.is_vintage()}")


main()
