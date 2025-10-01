"""
Rewrite password star program with functions
"""

#CONSTANTS
MINIMUM_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    password_stars = convert_password_to_stars(password)
    print(password_stars)


def convert_password_to_stars(password: str):
    #Function to convert the password into an equal amount of stars
    password_length = len(password)
    password_stars = "*" * password_length
    return password_stars


def get_password():
    #Get password from user
    password = input("Enter password: ")
    #Check if password is longer than minimum length
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        password = input(f"Password must be greater than {MINIMUM_PASSWORD_LENGTH} characters: ")
    return password


main()