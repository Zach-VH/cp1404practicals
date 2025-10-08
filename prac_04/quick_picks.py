"""
Creates a user specified number of lines containing 6 non-repeating digits between 1-45
"""
import random

def main():
    number_of_picks = int(input("How many quick picks: "))

    quick_picks = generate_quick_picks(number_of_picks)
    for pick in quick_picks:
        print(f"{pick[0]:>2} {pick[1]:>2} {pick[2]:>2} {pick[3]:>2} {pick[4]:>2} {pick[5]:>2}")


def generate_quick_picks(number_of_picks):
    quick_pick = []
    for line in range(0, number_of_picks):
        new_line = []
        for i in range(0, 6):
            number = random.randint(1, 45)
            while number in new_line:
                number = random.randint(1, 45)
            else:
                new_line.append(number)
        quick_pick.append([str(number) for number in sorted(new_line)])
    return quick_pick

main()