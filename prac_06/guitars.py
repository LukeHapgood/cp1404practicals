from prac_06.guitar import Guitar

guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    print("{} added.".format(guitar))

    guitars.append(guitar)

    name = input("Name: ")

print("\n... snip ...\n\nThese are my guitars:")
for i, guitar in enumerate(guitars):
    if guitar.is_vintage() is True:
        vintage_string = " (vintage)"
    else:
        vintage_string = ''

    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))