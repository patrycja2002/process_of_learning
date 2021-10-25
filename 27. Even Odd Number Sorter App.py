# While Loops Challenge 27: Even Odd Number Sorter App

print("Welcome to the Even Odd Number Sorter App")

running = True
while running:
    numbers = input("\nEnter in a string of numbers separated by a comma (,) : ")
    numbers = numbers.replace(' ', '')

    numbers_list = numbers.split(",")


    evens = []
    odds = []

    print("\n---- Result Summary ----")
    for number in numbers_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print("\t" + str(number) + " is even!")
        else:
            odds.append(number)
            print("\t" + str(number) + " is odd!")

    evens.sort()
    odds.sort()

    print("\nThe following " + str(len(evens)) + " numbers are even: ")
    for even in evens:
        print("\t" + str(even))

    print("\nThe following " + str(len(odds)) + " numbers are odd: ")
    for odd in odds:
        print("\t" + str(odd))

    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice != "y":
        running = False
        print("Thank you for using the program. Goodbye.")
