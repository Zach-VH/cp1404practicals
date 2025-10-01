"""
Determining the result from score using menu
"""

#import
from random import random

#CONSTANT
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Gets score from user and prints result"""
    print(MENU)
    choice = input(">>> ").upper()
    score = None
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            score_exist = check_score_exist(score)
            if score_exist:
                result = get_result(score)
                print(result)
        elif choice == "S":
            score_exist = check_score_exist(score)
            if score_exist:
                stars = create_stars(score)
                print(stars)
        else:
            print("Invalid Option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")

def get_score():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        score = float(input("Score must be between 0 and 100: "))
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

def check_score_exist(score):
    try:
        float(score)
    except TypeError:
        score_exist = False
        print("Score does not exist. Input score first.")
    else:
        score_exist = True
    return score_exist

def create_stars(score):
    stars = "*" * int(round(score))
    return stars


main()