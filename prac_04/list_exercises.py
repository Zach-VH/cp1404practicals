"""
Exercises on how to store and read arrays
"""

def main():
    """Gets 5 numbers from user and displays the first, last, smallest, largest and average of the list"""
    numbers = get_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {avg(numbers)}")


def get_numbers():
    numbers = []
    for i in range(1, 6):
        numbers.append(float(input(f"Enter number {i}: ")))
    return numbers


def avg(numbers):
    total = 0
    for number in numbers:
        total += number
    total /= len(numbers)
    return total


main()