"""
Wimbledon Open Champions
Estimated: 25 minutes
Actual (functioning): 32 minutes 29 seconds
"""

FILENAME = "wimbledon.csv"

def main():
    championships = load_championships()
    year_to_championship = convert_list_into_dictionary(championships)
    display_champions_number_of_wins(year_to_championship)
    display_list_of_countries(year_to_championship)


def display_list_of_countries(year_to_championship):
    countries = sorted(set(list(champion[1] for champion in year_to_championship.values())))
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))


def display_champions_number_of_wins(year_to_championship):
    champion_names = list(champion[0] for champion in year_to_championship.values())
    print("Wimbledon Champions:")
    for name in set(champion_names):
        print(f"{name}: {len([champion for champion in champion_names if champion == name])}")
    print()


def convert_list_into_dictionary(championships):
    year_to_championship = {}
    for championship in championships:
        year_to_championship[championship[0]] = [championship[2], championship[1]]
    return year_to_championship


def load_championships():
    championships = []
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        for line in in_file:
            championships.append(line.strip().split(","))
    championships.pop(0)
    return championships


main()