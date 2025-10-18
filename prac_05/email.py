"""
Emails to Names
Estimated: 15 minutes
Actual: 13 minutes 13 seconds
"""

ACCEPTED_CONFIRMATION_STATEMENT = ["Y",""]

def main():
    email_to_name = {}
    get_email_to_name(email_to_name)
    print_email_to_name(email_to_name)


def print_email_to_name(email_to_name):
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_email_to_name(email_to_name):
    email = input("Email: ")
    while email != "":
        if email in list(email_to_name.keys()):
            confirmation = input(f"Is your name {email_to_name[email]}?").upper()
            if confirmation not in ACCEPTED_CONFIRMATION_STATEMENT:
                email_to_name[email] = input("Name: ")
        else:
            email_to_name[email] = input("Name: ")
        email = input("Email: ")


main()