""" display menu
    get choice
    while choice != quit option
        if choice == first option
            do first task
        else if choice == <second option>
            do second task
    ...
        else if choice == <n-th option>
            do n-th task
        else
            display invalid input error message
        display menu
        get choice
do final thing, if needed"""

MENU = """Menu:
1 - Option 1
2 - Option 2
Q - Quit"""

print(MENU)
menu_input = input()
while menu_input != "Q":
    if menu_input == "1":
        print("You have chosen option 1")
    elif menu_input == "2":
        print("You have chosen option 2")
    else:
        print("Invalid Input")
    print(MENU)
    menu_input = input()