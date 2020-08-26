"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score != 1000:
    if score < 0:
        print("Invalid score")
    elif score > 100:
            print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))