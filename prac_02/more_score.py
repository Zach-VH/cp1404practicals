"""
CP1404/CP5632 - Practical
Program to create a set number of random score status
"""

#import
from random import random


def main():
    """Print as many scores results as the user asks"""
    number_of_scores = int(input("Enter number of random scores you want: "))
    for i in range(number_of_scores):
        score = get_random_score()
        result = get_result(score)
        print(f"{i+1}. {score} is a {result} score")

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