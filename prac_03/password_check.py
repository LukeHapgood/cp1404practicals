
min_length = 4

def main():

    password = get_password(min_length)

    hidden_password(password)


def hidden_password(password):
    print("*" * len(password))


def get_password(min_length):
    valid = False
    print("Your password must contain at least {} characters".format(min_length))
    password = input("Please enter a valid password: ")
    while not valid:
        if len(password) >= min_length:
            valid = True
        else:
            print("Invalid password!")
            password = input("Please enter a valid password: ")
    return password


main()