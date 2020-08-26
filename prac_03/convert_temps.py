

def main():
    temperatures = open("temps_input.txt", 'r')
    output = open("temps_output.txt", 'w')
    lines = temperatures.readlines()
    for line in lines:
        line = float(line)
        print(fahrenheit_to_celsius(line), file=output)

    output.close()
    temperatures.close()


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
