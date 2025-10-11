"""
Check the username from the user with the authorised user list for authorisation
"""

USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    username = input("Enter your username: ")
    is_authorised = authorise_user(username)
    check_authorisation(is_authorised)


def check_authorisation(is_authorised: bool):
    """Check if the authorisation is true and print access"""
    if is_authorised:
        print("Access Granted")
    else:
        print("Access Denied")


def authorise_user(username: str) -> bool:
    """Check the username entered with the list of authorised users"""
    is_authorised = False
    for auth_user in USERNAMES:
        if auth_user == username:
            is_authorised = True
            break
    return is_authorised


main()