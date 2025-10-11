"""
CP1404 - Strings in a list
Gets a list of strings from a user and finds a repeating string
"""


def main():
    """Prints string if the string repeated"""
    strings = get_strings()
    repeated_string = check_repeating_string(strings)
    print_repeated_strings(repeated_string)

def get_strings():
    """Get a list of strings from user until nothing is entered"""
    strings = []
    string = input("Enter string 1: ")
    while string != "":
        strings.append(string)
        string = input(f"Enter string {len(strings)+1}: ")
    return strings

def check_repeating_string(strings):
    """Check if string is repeated and return unique repeated strings"""
    repeated_string = []
    for index,string in enumerate(strings,0):
        strings.pop(index)
        if string in strings:
            repeated_string.append(string)
    return set(repeated_string)


def print_repeated_strings(repeated_string):
    """Prints repeated strings if it exists"""
    if repeated_string:
        print(f"Strings repeated: {", ".join(repeated_string)}")
    else:
        print("No string is repeated")


main()