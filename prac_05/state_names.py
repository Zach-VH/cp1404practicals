"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
CODE_WIDTH = max(len(name) for name in list(CODE_TO_NAME.keys()))
NAME_WIDTH = max(len(name)for name in list(CODE_TO_NAME.values()))



state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:{CODE_WIDTH}} is {CODE_TO_NAME[state_code]:{NAME_WIDTH}}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code in CODE_TO_NAME:
    print(f"{state_code:{CODE_WIDTH}} is {CODE_TO_NAME[state_code]:{NAME_WIDTH}}")