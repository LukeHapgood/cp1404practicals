for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()
print()
''' print n lines of increasing stars.
Using the same number as above print lines of increasing stars, starting at 1. 
E.g. if 4 was the number entered, your single loop should print
*
**
***
****'''
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()
for i in range(1, stars+1):
    print("*" * i)