"""
Warm Up
Practicing how to read arrays
"""

numbers = [3,1,4,1,5,9,2]

print(numbers[0])           #Guess:  3                          Actual: 3
print(numbers[-1])          #Guess:  out of range of index      Actual: 2
print(numbers[3])           #Guess:  1                          Actual: 1
print(numbers[:-1])         #Guess:  9                          Actual: [3,1,4,1,5,9]
print(numbers[3:4])         #Guess:  1,5                        Actual: [1]
print(5 in numbers)         #Guess:  4                          Actual: True
print(7 in numbers)         #Guess:  does not exist in list     Actual: False
print("3" in numbers)       #Guess:  does not exist in list     Actual: False
print(numbers + [6, 5, 3])  #Guess:  [3,1,4,1,5,9,2,6,5,3]      Actual: [3,1,4,1,5,9,2,6,5,3]