import random

number_of_quick_picks = int(input("How many quick picks? "))
output_list = []

for i in range(number_of_quick_picks):
    quick_pick = [random.randint(1, 45) for i in range(6)]
    quick_pick.sort()
    output_list.append(quick_pick)

for line in range(len(output_list)):
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(*output_list[line]))
