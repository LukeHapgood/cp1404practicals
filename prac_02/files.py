# Program 1
name_output = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=name_output)
name_output.close()

# Program 2
name_output = open("name.txt", 'r')
print("Your name is", name)
name_output.close()

# Program 3
numbers_file = open("numbers.txt", 'r')
first_number = int(numbers_file.readline())
second_number = int(numbers_file.readline())
print(first_number + second_number)
numbers_file.close()

# Program 4
numbers_file = open("numbers.txt", 'r')
lines = numbers_file.readlines()
numbers_file.close()
total = 0
for i in range(len(lines)):
    total += int(lines[i])
print(total)
