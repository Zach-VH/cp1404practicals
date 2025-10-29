"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(f"{my_car} \n")

    #Exercise to create car object "Limo"
    limo = Car("limo",100)
    print(f"Limo currently has {limo.fuel} units of fuel")
    print("Filling 20 units of fuel into limo")
    limo.add_fuel(20)
    print(f"Limo currently has {limo.fuel} units of fuel")
    print(f"Attempting to drive 115 km in limo")
    limo.drive(115)
    print(f"Limo currently has {limo.fuel} units of fuel")
    print(limo)



main()