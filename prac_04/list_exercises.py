"""
Exercises on how to store and read arrays
"""

def main():
    """Gets user inputted number of numbers from user and displays the first, last, smallest, largest and average of the list"""
    print("Number set exercise. Enter any amount of number until you enter \'0\'")
    numbers = get_numbers()
    print(f"You entered {len(numbers)} numbers")
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {avg(numbers)}")


def get_numbers():
    """Get user inputted numbers"""
    numbers = []
    number = float(input(f"Enter number 1: "))
    while number != 0:
        numbers.append(number)
        number = float(input(f"Enter number {len(numbers)+1}: "))
    return numbers


def avg(numbers):
    """Takes the sum of all numbers and divide by the length of the number set"""
    total = 0
    for number in numbers:
        total += number
    total /= len(numbers)
    return total


main()