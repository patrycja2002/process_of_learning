# Functions Challenge 31: The Python Dice App
import random


def dice_sides():
    sides = int(input("\nHow many sides would you like on your dice: "))
    return sides


def dice_number():
    number = int(input("How many dice would you like to roll: "))
    return number


def roll_dice(number, sides):
    dice = []
    print("You rolled", str(number), "", str(sides), "sided dice.")
    print("-----Results are as followed-----")
    for x in range(number):
        value = random.randint(1, sides)
        print("\t" + str(value))
        dice.append(value)
    return dice


def sum_dice(dice):
    total = 0
    for i in dice:
        total += i
    print("The total value of your roll is " + str(total) + ".")


def roll_again():
    choice = input("\nWould you like to roll again (y/n): ").lower()
    if choice != 'y':
        roll = False
    else:
        roll = True
    return roll


print("Welcome to the Python Dice App")
rolling = True
while rolling:
    d_sides = dice_sides()
    d_number = dice_number()

    r_dice = roll_dice(d_sides, d_number)
    sum_dice(r_dice)

    rolling = roll_again()

print("\nThank you for using the Python Dice App.")
