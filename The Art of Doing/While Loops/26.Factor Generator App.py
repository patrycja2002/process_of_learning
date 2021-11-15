# While Loops Challenge 26: Factor Generator App

print("Welcome to the Factor Generator App")

running = True

while running:
    number = int(input("\nEnter a number to determine all factors of that number: "))
    factors = []
    for x in range(1, number+1):
        if number % x == 0:
            factors.append(x)
    print("\nFactors of " + str(number) + " are: ")
    for y in factors:
        print(y)

    print("\nIn summary: ")
    for x in range(int(len(factors)/2)):
        print(str(factors[x]) + " * " + str(factors[-x-1]) + " = " + str(number))

    choice = input("\nRun again (y/n): ").lower()
    if choice != "y":
        running = False
        print("Thank you for using the program. Have a great day.")
