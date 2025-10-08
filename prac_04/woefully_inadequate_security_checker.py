"""
Check the username from the user with the authorised user list for authorisation
"""

USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    username = input("Enter your username: ")
    is_authorised = False
    for auth_user in USERNAMES:
        if auth_user == username:
            is_authorised = True
            break

    if is_authorised:
        print("Access Granted")
    else:
        print("Access Denied")


main()