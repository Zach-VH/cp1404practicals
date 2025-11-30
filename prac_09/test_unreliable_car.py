"""
Prac 9
Test Unreliable Car Class
"""
from unreliable_car import UnreliableCar

my_car = UnreliableCar('Ford Fiesta',150,30)
print(my_car)

number_of_attempts = 0
while my_car.fuel == 150:
    number_of_attempts += 1
    print(f"Attempt {number_of_attempts} to drive car")
    distance = my_car.drive(50)
    if distance == 0:
        print("Attempt failed... \n")
print(f"Success! {my_car.name} has driven 50 km \n")

print("Test drive car 100 times")
number_of_successes = 0
number_of_failures = 0
for i in range(0,100):
    distance = my_car.drive(1)
    if distance == 0:
        number_of_failures += 1
    else:
        number_of_successes += 1
print(f"Number of successes: {number_of_successes:<4}")
print(f"Number of failures: {number_of_failures:<4}")