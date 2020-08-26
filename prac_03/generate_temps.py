import random

output_file = open("temps_input.txt", 'w')
for i in range(15):
    print(random.uniform(-200, 200), file=output_file)
output_file.close()
