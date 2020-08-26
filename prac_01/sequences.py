
import math

lower: int = int(input("Lower Boundary: "))
upper: int = int(input("Upper Boundary: "))

while lower > upper:
    print("The lower boundary must be less than the upper boundary")
    lower = int(input("Lower Boundary: "))
    upper = int(input("Upper Boundary: "))

MENU = """Menu:
E - Show EVEN numbers from {0} to {1}
O - Show ODD numbers from {0} to {1}
S - Show SQUARE numbers from {0} to {1}
B - Change your Boundaries 
Q - Quit""".format(lower, upper)

print(MENU)
menu_input = input()
while menu_input != "Q":
    if menu_input == "E":
        # Print all the even numbers
        if lower % 2 == 0:
            for i in range(lower, upper + 1, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(lower+1, upper + 1, 2):
                print(i, end=' ')
            print()
    elif menu_input == "O":
        # Print all the odd numbers
        if lower % 2 == 0:
            for i in range(lower + 1, upper + 1, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(lower, upper + 1, 2):
                print(i, end=' ')
            print()
    elif menu_input == "S":
        # Print all the square numbers
        for i in range(lower, upper):
            if math.sqrt(i) % 1 == 0:
                print(i, end=' ')
    elif menu_input == "B":
        # Change the boundaries
        lower = int(input("Lower Boundary: "))
        upper = int(input("Upper Boundary: "))

        while lower > upper:
            print("The lower boundary must be less than the upper boundary")
            lower = int(input("Lower Boundary: "))
            upper = int(input("Upper Boundary: "))
        MENU = """Menu:
E - Show EVEN numbers from {0} to {1}
O - Show ODD numbers from {0} to {1}
S - Show SQUARE numbers from {0} to {1}
B - Change your Boundaries 
Q - Quit""".format(lower, upper)
    else:
        print("Invalid Input")
    print(MENU)
    menu_input = input()
