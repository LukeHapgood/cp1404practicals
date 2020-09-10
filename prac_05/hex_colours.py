
COLOUR_TO_CODE = {"limegreen": "#32cd32", "lightcoral": "#f08080", "lavender": "#e6e6fa", "deepskyblue2": "#00b2ee",
                "darkorchid": "#9932cc", "goldenrod": "#daa520", "ghostwhite": "#f8f8ff", "dodgerblue2": "#1c86ee",
                "firebrick1": "#ff3030", "seagreen3": "#43cd80"}

colour = input("Enter colour: ")
while colour != "":
    if colour.casefold() in COLOUR_TO_CODE:
        print("{}'s code is {}".format(colour, COLOUR_TO_CODE[colour.casefold()]))
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
