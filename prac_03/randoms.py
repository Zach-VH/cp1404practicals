import random

print(random.randint(5, 20))  # line 1: produces a whole number between 5 and 20 including both endpoints
print(random.randrange(3, 10, 2))  # line 2: produces an odd number between 3 and 10 including 3
                                                   # As line 2 produces odd numbers, it cannot produce a 4
print(random.uniform(2.5, 5.5))  # line 3: produces a 16 point float between and including 2.5 and 5.5

print(random.randint(1,100)) #Assuming number is whole
print(random.uniform(1,100)) #Assuming number is not whole
