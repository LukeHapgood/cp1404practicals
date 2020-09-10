
emails = {}

email = input("Email: ")
while email != "":
    if email in emails:
        print("{}'s email is already stored".format(emails[email]))
    else:
        name = email.split("@")[0]
        name = ''.join(character for character in name if not character.isdigit())
        if "." in name:
            name_list = name.split(".")
            name = (" ".join(name_list)).title()

        confirm = input("Is your name {}? (y,n) ".format(name.title()))
        complete = False
        while not complete:
            if confirm.casefold() in {"yes", "y"}:
                emails[email] = name.title()
                complete = True
            elif confirm.casefold() in {"no", "n"}:
                name = input("Name: ")
                emails[email] = name.title()
                complete = True
            else:
                print("Invalid input")
                confirm = input("Is your name {}? (y,n) ".format(name.title()))
    email = input("Enter email: ")

print(emails)
for email, name in sorted(emails.items()):
    print("{} ({})".format(name, email))
