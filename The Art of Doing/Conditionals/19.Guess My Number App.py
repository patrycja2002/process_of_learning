# Conditionals Challenge 19: Guess My Number App
import random

print("Welcome to the Guess My Number App")

name = input("\nHello! What is your name: ").title()
print("Well", str(name), ", I am thinking of a number between 1 and 20.")

number = random.randint(1, 20)

for x in range(5):
    guess = int(input("\nTake a guess: "))
    if number > guess:
        print("Your guess is too low.")
    elif number < guess:
        print("Your guess is too high.")
    else:
        break

if guess == number:
    print("Good job,",name,  "! You guessed my number in", str(x+1), "guesses!")
else:
    print("\nGame Over. The number I was thinking of was " + str(number) + ".")
