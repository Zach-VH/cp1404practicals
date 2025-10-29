"""
Test area for guitar class
"""

from guitar import Guitar

guitars = [Guitar("Gibson L-5 CES",1922,16035.40),
           Guitar("Another Guitar",1975,16035.40)]

print(f"{guitars[0].name} get_age() - Expected 103. Got {guitars[0].get_age()}.")
print(f"{guitars[1].name} get_age() - Expected 5. Got {guitars[1].get_age()}.")
print(f"{guitars[0].name} is_vintage() - Expected True. Got {guitars[0].is_vintage()}.")
print(f"{guitars[1].name} is_vintage() - Expected True. Got {guitars[1].is_vintage()}. (Edge Case)")


