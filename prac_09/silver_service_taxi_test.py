"""
Prac 9
Silver Service Taxi Class Test
"""
from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi('Hummer',200,2)
print(my_taxi)

my_taxi.drive(18)
# print(f"Fare: ${my_taxi.get_fare()}")
assert my_taxi.get_fare() == 48.80