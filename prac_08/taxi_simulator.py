"""
CP1404/CP5632 Practical - Suggested Solution
Taxi simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = taxis[0]  # Default

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            list_taxis(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]

        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = input("Drive how far? ")
            current_taxi.drive(distance_to_drive)
            fare = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
            total_bill += fare

        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
