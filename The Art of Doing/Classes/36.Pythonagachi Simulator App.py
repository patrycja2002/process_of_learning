# Classes Challenge 36: Pythonagachi Simulator App
import random


class Creature:
    def __init__(self, name):
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0:
            self.food -= 1
            hunger = random.randint(1, 4)
            self.hunger -= hunger
            print("Yum! " + self.name + " ate a great meal!")
        else:
            print(self.name + " doesn't have any food! Better forage for some.")

        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        number = random.randint(0, 2)
        print("\n" + self.name + " wants to play a game.")
        print(self.name + " is thinking of a number 0, 1, or 2.")
        guess = int(input("What is your guess: "))

        if guess == number:
            print("That is correct!!!")
            self.boredom -= 3
        else:
            print("WRONG! " + self.name + " was thinking of " + str(number) + ".")
            self.boredom -= 1

        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print("Zzzzzzz.....Zzzzzzz.....Zzzzzzz.....")
        if self.tiredness < 0:
            self.tiredness = 0

        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        number = random.randint(0, 2)
        if number == 0:
            print(self.name + " just woke up!")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print(self.name + " won't wake up...")
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(self.name + "has taken a bath. All clean!")

    def forage(self):
        food_found = random.randint(0, 4)
        self.hunger += food_found
        self.dirtiness += 2
        print(self.name + "found" + str(food_found) + "pieces of food!")

    def show_values(self):
        print("\nCreature Name: " + self.name)
        print("Hunger (0-10): " + str(self.hunger))
        print("Boredom (0-10): " + str(self.boredom))
        print("Tiredness (0-10): " + str(self.tiredness))
        print("Dirtiness (0-10): " + str(self.dirtiness))
        print("\nFood Inventory: " + str(self.food) + " pieces")
        if self.is_sleeping:
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")

    def incriment_values(self, num):
        self.hunger += random.randint(0, num)

        if self.is_sleeping == False:
            self.boredom += random.randint(0, num)
            self.tiredness += random.randint(0, num)
            self.dirtiness += random.randint(0, num)

    def kill(self):
        if self.hunger >= 10:
            print(self.name + " has starved to death...")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(self.name + " has suffered an infection and died...")
            self.is_alive = False
        elif self.boredom >= 10:
            print(self.name + " is bored. Falling asleep...")
            self.is_alive = True
        elif self.tiredness >= 10:
            print(self.name + " is bored. Falling asleep...")
            self.is_sleeping = True


def show_menu(creature):
    if creature.is_sleeping:
        choice = input("\nEnter (6) to try and wake up: ")
        choice = "6"
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        choice = input("What is your choice: ")
    return choice


def call_action(creature, choice):
    if choice == "1":
        creature.eat()
    elif choice == "2":
        creature.play()
    elif choice == "3":
        creature.sleep()
    elif choice == "4":
        creature.clean()
    elif choice == "5":
        creature.forage()
    elif choice == "6":
        creature.awake()
    else:
        print("Sorry, that is not a valid move.")


print("Welcome to the Pythonagachi Simulator App")
difficulty = int(input("Please choose a difficulty level (1-5): "))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

running = True
while running:
    name = input("What name would you like to give your pet Pythonagachi: ")
    player = Creature(name)

    rounds = 1
    while player.is_alive:
        print("----------------------------------------------------------------------------")
        print("Round #" + str(rounds))
        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)

        print("\nRound #" + str(rounds) + " Summary: ")

        player.show_values()
        input("\nPress (enter) to continue...")
        player.incriment_values(difficulty)
        player.kill()

        rounds += 1

    print("\nR.I.P.")
    print(player.name + " survived a total of " + str(rounds - 1) + " rounds.")
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        running = False
    print("Thank you for playing Pythonagachi!")


