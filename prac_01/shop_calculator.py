""" Input number of items
    request price of each item
    sum prices
    print result """
number_items: int = int(input("Number of items: "))
while number_items <= 0:
    print("Invalid number of items!")
    number_items: int = int(input("Number of items: "))
total: float = 0
for item in range(number_items):
    price: float = float(input("Price of item: $"))
    total += price
print("Total price for the {} items is: ${:.2f}".format(number_items, total))
