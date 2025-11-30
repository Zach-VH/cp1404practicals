"""
CP1404 Practice
Hexcode for colours in a dictionary

"""

COLOUR_NAME_TO_HEX = {"aliceblue": "#f0f8ff", "gray7": "#121212", "lawngreen": "#7cfc00", "lemoncurry": "#cca01d",
                      "persianred": "#cc3333", "lilac": "#c8a2c8", "russianviolet": "#32174d", "rust": "#b7410e",
                      "pumpkin": "#ff7518", "maroon": "#b03060"}

colour_name = input("Enter colour name: ").lower().replace(' ',"")
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower().replace(' ',"")

