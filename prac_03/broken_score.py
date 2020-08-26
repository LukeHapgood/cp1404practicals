"""Program to determine score status"""


def main():
    completed = False
    while not completed:
        try:
            score = int(input("Enter score: "))
            if score < 0:
                print("{} is an invalid score".format(score))
            elif score > 100:
                print("{} is an invalid score".format(score))
            else:
                test_score(score)
                completed = True
        except ValueError:
            print("Please input an integer")

    import random
    random_score = random.randint(0, 100)
    test_score(random_score)


def test_score(score):
    if score >= 90:
        print("{} is Excellent".format(score))
    elif score >= 50:
        print("{} is Passable".format(score))
    else:
        print("{} is Bad".format(score))


main()
