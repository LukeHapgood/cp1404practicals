
import random


def main():
    results_output = open("results.txt", 'w')
    no_of_scores = int(input("How many scores would you like too generate? "))
    for i in range(no_of_scores):
        random_score = random.randint(0, 100)
        test_score(random_score, results_output)
    results_output.close()


def test_score(score, output):
    if score >= 90:
        print("{} is Excellent".format(score), file=output)
    elif score >= 50:
        print("{} is Passable".format(score), file=output)
    else:
        print("{} is Bad".format(score), file=output)


main()
