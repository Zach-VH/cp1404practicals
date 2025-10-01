"""
Rewrite password star program with functions
"""

MINIMUM_PASSWORD_LENGTH = 8

password = input("Enter password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    password = input(f"Password must be greater than {MINIMUM_PASSWORD_LENGTH} characters: ")
password_length = len(password)
password_stars = "*" * password_length
print(password_stars)
