"""
Guitars list
Estimate: 22 minutes
Actual: 28 minutes

Added checks for user inputs
Updated time: 48 minutes
"""
from prac_06.guitar import Guitar

def main():
    """Allow users to save guitars into a list and print out the list of guitars"""
    print("My guitars!")
    guitars = get_guitars()
    print_guitar_list(guitars)


def print_guitar_list(guitars):
    """Prints the list of guitars the user inputted and list if there are vintage"""
    print("\nThese are my guitars:")
    max_name_width = max(len(guitar.name) for guitar in guitars)
    max_cost_width = max(len(str(guitar.cost)) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (is vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i} : {guitar.name:>{max_name_width}} ({guitar.year:4}), worth $ {guitar.cost:<{max_cost_width}}{vintage_string}")


def get_guitars():
    """Gets a list of guitars collected from the user"""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_year()
        cost = get_cost()
        guitars.append(Guitar(name, year, cost))
        print(guitars[-1])
        name = input("\nName: ")
    return guitars


def get_cost():
    """Get the cost of the guitar, checking if it's a valid cost"""
    cost = -1
    while cost == -1:
        try:
            cost = round(float(input("Cost: $")), 2)
            if cost <= 0:
                print("Year must be greater than 0")
                cost = -1
        except ValueError:
            print("Year must be a decimal number")
    return cost


def get_year():
    """Get the year the guitar was created, checking if it's a valid year"""
    year = -1
    while year == -1:
        try:
            year = int(input("Year: "))
            if year <= 0 or year > 2025:
                print("Year must be greater than 0 and less than 2025")
                year = -1
        except ValueError:
            print("Year must be a whole number")
    return year

main()