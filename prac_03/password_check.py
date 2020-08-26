
min_length = 4
valid = False

print("Your password must exceed {} characters".format(min_length))
password = input("Please enter a valid password: ")

while not valid:
    if len(password) >= min_length:
        print("*"*len(password))
        valid = True
    else:
        print("Invalid password!")
        password = input("Please enter a valid password: ")