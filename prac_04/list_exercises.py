numbers = []
for i in range(5):
    i = int(input("Number: "))
    numbers.append(i)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))

average = sum(numbers) / len(numbers)
print("The average of the numbers is {}".format(average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_username = input("Input your username >>>")
if input_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
