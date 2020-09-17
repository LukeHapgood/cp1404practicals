from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
guitar_2 = Guitar("Another Guitar", 2013, 249.95)

age = gibson.get_age()
vintage = gibson.is_vintage()
print("{} get_age() - Expected {}. Got {}".format(gibson.name, 98, age))
print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, vintage))

age = guitar_2.get_age()
vintage = guitar_2.is_vintage()
print("{} get_age() - Expected {}. Got {}".format(guitar_2.name, 7, age))
print("{} is_vintage() - Expected {}. Got {}".format(guitar_2.name, False, vintage))