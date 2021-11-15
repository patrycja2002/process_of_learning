# While Loops Challenge 28: Prime Number App
import time

print("Welcome to the Prime Number App")

running = True

while running:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")

    if choice == "1":
        number_prime = int(input("\nEnter a number to determine if it is prime or not: "))

        prime_status = True
        for x in range(2, number_prime):
            if number_prime % x == 0:
                prime_status = False
                break

        if prime_status:
            print(str(number_prime), "is prime!")
        else:
            print(str(number_prime), "is not prime!")
    elif choice == "2":
        lower = int(input("\nEnter the lower bound of your range: "))
        upper = int(input("Enter the upper bound of your range: "))
        primes = []

        start_time = time.time()
        for i in range(lower, upper + 1):
            if i > 1:
                prime_status = True
                for x in range(2, i):
                    if i % x == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            if prime_status:
                primes.append(i)

        end_time = time.time()

        delta_time = round(end_time - start_time, 4)

        print("\nCalculations took a total of", str(delta_time), "seconds.")
        print("The following numbers between", str(lower), "and", str(upper), "are prime:")
        input("Press enter to continue.")

        for i in primes:
            print(i)
    else:
        print("\nThat is not a valid option.")

    option = input("Would you like to run the program again (y/n): ")

    if option != "y":
        running = False
        print("\nThank you for using the program. Have a nice day.")

