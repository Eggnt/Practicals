
def main():
    champion_to_victories = {}
    countries_of_champions = set()
    championship_datasets = read_data()
    get_champions_and_countries(champion_to_victories, championship_datasets, countries_of_champions)
    number_of_countries = len(countries_of_champions)
    print_champions_and_countries(champion_to_victories, countries_of_champions, number_of_countries)


def print_champions_and_countries(champion_to_victories, countries_of_champions, number_of_countries):
    print("Wimbledon Champions:")
    for champion, number_of_victories in champion_to_victories.items():
        print(f"{champion} {number_of_victories}")
    print(f"These {number_of_countries} countries have won Wimbledon:\n{', '.join(sorted(countries_of_champions))}")


def get_champions_and_countries(champion_to_victories, championship_datasets, countries_of_champions):
    for year in championship_datasets:
        champion = year[2]
        country = year[1]
        champion_to_victories[champion] = champion_to_victories.get(champion, 0) + 1
        countries_of_champions.add(country)


def read_data():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        championship_datasets = [line.strip("\n").split(",") for line in in_file]
        championship_datasets.pop(0)
    return championship_datasets


main()
