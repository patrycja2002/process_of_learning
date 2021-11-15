# Functions Challenge 32: The Python Calculator App

def add(a, b):
    total = round(a+b, 4)
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(total) + ".")
    return str(a) + " + " + str(b) + " = " + str(total)


def subtract(a, b):
    difference = round(a-b, 4)
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(difference) + ".")
    return str(a) + " - " + str(b) + " = " + str(difference)


def multiply(a, b):
    product = round(a*b, 4)
    print("The product of " + str(a) + " and " + str(b) + " is " + str(product) + ".")
    return str(a) + " * " + str(b) + " = " + str(product)


def divide(a, b):
    if b != 0:
        quotient = round(a/b, 4)
        print("The quotient of " + str(a) + " and " + str(b) + " is " + str(quotient) + ".")
        return str(a) + " / " + str(b) + " = " + str(quotient)
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"


def exponent(a, b):
    power = round(a**b, 4)
    print("The result of " + str(a) + " and " + str(b) + " is " + str(power) + ".")
    return str(a) + " / " + str(b) + " = " + str(power)


print("Welcome to The Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
running = True
while running:
    num_1 = int(input("\nEnter a number: "))
    num_2 = int(input("Enter a number: "))
    operator = input("Enter an operation (addition, subtraction, " 
                      "multiplication, division, or exponentiation): ").lower()

    if operator == "addition" or operator == "a":
        result = add(num_1, num_2)
    elif operator == 'subtraction' or operator == 's':
        result = subtract(num_1, num_2)
    elif operator == 'multiplication' or operator == 'm':
        result = multiply(num_1, num_2)
    elif operator == 'division' or operator == 'd':
        result = divide(num_1, num_2)
    elif operator == 'exponentiation' or operator == 'e':
        result = exponent(num_1, num_2)
    else:
        print("That is not a valid operation. Try again.")
        result = "OPP ERROR"

    history.append(result)
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        print("\nCalculation Summary: ")
        for x in history:
            print(x)
        print("\nThank you for using the Python Calculator App. Goodbye.")
        running = False
