# Conditionals Challenge 17: Coin Toss App
import random

print("Welcome to the Coin Toss App")

print("\nI will flip a coin a set number of times.")

f_number = int(input("How many times would you like me to flip the coin: "))
choice = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping!!!\n")

heads = 0
tails = 0

for x in range(f_number):
    coin = random.randint(0, 1)

    if coin == 1:
        heads += 1
        if choice.startswith("y"):
            print("HEADS")
    else:
        tails += 1
        if choice.startswith("y"):
            print("TAILS")

    if heads == tails:
        print("At " + str(x + 1) + " flips, the number of heads and tails were equal at " + str(heads) + "each.")
h_percent = round(100*heads/f_number, 2)
t_percent= round(100*tails/f_number, 2)
print("\nResults Of Flipping A Coin ", f_number, "Times:")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t" + str(heads) + "/" + str(f_number) + "\t\t" + str(h_percent) + "%")
print("Tails\t\t" + str(tails) + "/" + str(f_number) + "\t\t" + str(t_percent) + "%")