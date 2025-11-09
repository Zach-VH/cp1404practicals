"""
Estimated (total): 30 minutes

Code:
Documentation:
Actual:
"""
from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    guitars = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0],int(parts[1]),round(float(parts[2]),2))
            guitars.append(guitar)
    print(guitars)
    guitars.sort()
    print(guitars)




main()