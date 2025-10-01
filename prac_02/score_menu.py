"""
Determining the result from score using menu
"""

#import
from random import random

def main():
    """Gets score from user and prints result"""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    #Creates a random score and evaluates result
    score = get_random_score()
    print(f"Creating random score: {score}")
    result = get_result(score)
    print(result)

def get_random_score():
    """Creates a random score between 0 and 100"""
    score = round(random() * 100,2)
    return score


def get_result(score: float):
    """Get result from score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()