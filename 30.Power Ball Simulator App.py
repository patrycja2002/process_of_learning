# While Loops Challenge 30: Power Ball Simulator App
import random

print("--------------------Power-Ball Simulator--------------------")

white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))

if white_balls < 5:
    white_balls = 5

red_balls = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))

if red_balls < 1:
    red_balls = 1

odds = 1

for x in range(5):
    odds *= white_balls - x

odds *= red_balls/120

print("You have a 1 in " + str(odds) + " chance of winning this lottery.")

ticket_interval = int(input("Purchase tickets in what interval: "))

winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1, white_balls)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

number = random.randint(1, red_balls)
winning_numbers.append(number)

print("---------Welcome to the Power-Ball-----------")
print("\nTonight's winning numbers are: ", end="")
for number in winning_numbers:
    print(str(number), end=' ')

input("\nPress 'Enter' to begin purchasing tickets!!!")

tickets_purchased = 0
running = True
tickets_sold = []

while winning_numbers not in tickets_sold and running == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        number = random.randint(1, white_balls)
        if number not in lottery_numbers:
            lottery_numbers.append(number)

    lottery_numbers.sort()
    number = random.randint(1, red_balls)
    lottery_numbers.append(red_balls)

    if number not in tickets_sold:
        tickets_purchased += 1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)

    else:
        print("Losing ticket generated; disregard...")

    if tickets_purchased % ticket_interval == 0:
        print(str(tickets_purchased), "tickets purchased so far with no winners...")
        choice = input("Keep purchasing tickets (y/n):")
        if choice != "y":
            running = False

if lottery_numbers == winning_numbers:
    print("\nWinning ticket numbers: ", end='')
    for number in lottery_numbers:
        print(str(number), end=' ')
    print("\nPurchased a total of " + str(tickets_purchased) + " tickets.")
else:
    print("\nYou bought " + str(tickets_purchased) + " tickets and still lost!")
    print("Better luck next time!")
