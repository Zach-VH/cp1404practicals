"""
Load Guitar from csv file and display it
Estimated (total): 30 minutes

Code: 24 minutes 07 seconds
Documentation: 6 minutes 31 seconds
Actual: 30 minutes 38 seconds
"""

# Imports
from guitar import Guitar

# CONSTANTS
FILENAME = "guitars.csv"

def main():
    """Get list of guitars from csv file, displays list and sorts by year, prompts user to add guitar and saves in csv file"""
    #Get list of guitars and header from csv file
    guitars, header = get_guitars()
    # print(guitars)
    guitars.sort()
    print(guitars)

    add_guitars(guitars)

    save_guitars(guitars, header)


def add_guitars(guitars):
    """Gets a list of guitars collected from the user and append to guitar list. Stops prompting user when entering ''
        in name prompt"""
    name = input("Name: ")
    while name != "":
        year = get_year()
        cost = get_cost()
        guitars.append(Guitar(name, year, cost))
        print(guitars[-1])
        name = input("\nName: ")

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

def get_guitars():
    """Reads the csv file and get all guitars in the file as a list of objects, get header of csv as well"""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        # Get header from first line
        header = in_file.readline().strip()
        # Ever other line has guitar info in it
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), round(float(parts[2]), 2))
            guitars.append(guitar)
    return guitars, header

def save_guitars(guitars,header):
    """Overwrites into the csv file with the updated list of guitars"""
    with open(FILENAME, 'w') as out_file:
        # Using previous header for the first line
        print(header, file=out_file)
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}",file=out_file)

main()