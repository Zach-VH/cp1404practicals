"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
MIN_UPPERCASE = 1
MIN_LOWERCASE = 1
MIN_DIGIT = 1
MIN_SPECIAL_CHARACTER = 1
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print(f"\t{MIN_UPPERCASE} or more uppercase characters")
    print(f"\t{MIN_LOWERCASE} or more lowercase characters")
    print(f"\t{MIN_DIGIT} or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"\tand {MIN_SPECIAL_CHARACTER} or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if MIN_LENGTH > len(password) or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        pass

    if number_of_digit < MIN_DIGIT:
        return False
    if number_of_lower < MIN_LOWERCASE:
        return False
    if number_of_upper < MIN_UPPERCASE:
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special < MIN_SPECIAL_CHARACTER:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()