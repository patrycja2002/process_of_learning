# Classes Challenge 38: Pykemon Simulation App
import random


class Pykemon:
    def __init__(self, name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        damage = random.randint(15, 25)
        print("Pykemon " + self.name + " used " + self.moves[0] + ".")
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print("Pykemon " + self.name + " used " + self.moves[1] + ".")
        if damage < 10:
            print("The attack missed!!!")
        else:
            print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage

    def restore(self):
        heal = random.randint(15, 25)
        print("Pykemon " + self.name + " used " + self.moves[2] + ".")
        print("It healed " + str(heal) + " health points.")
        self.current_health -= heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print("Pykdfsfgsdfemon " + self.name + " has fainted!")
            input("Press Enter to continue.")

    def show_stats(self):
        print("\nName: " + self.name)
        print("Element Type: " + self.element)
        print("Health: " + str(self.current_health) + " / " + str(self.max_health))
        print("Speed: " + str(self.speed))


class Fire(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self, enemy):
        print("Pykemon " + self.name + " used " + self.moves[3].upper() + "!")
        if enemy.element == "GRASS":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "WATER":
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage

    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")
        print("-- " + self.moves[3] + " --")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")


class Water(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]

    def special_attack(self, enemy):
        print("Pykemon " + self.name + " used " + self.moves[3].upper() + "!")
        if enemy.element == "FIRE":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "GRASS":
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 20)
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage

    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")
        print("-- " + self.moves[3] + " --")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


class Grass(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]

    def special_attack(self, enemy):
        print("Pykemon " + self.name + " used " + self.moves[3].upper() + "!")
        if enemy.element == "WATER":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "FIRE":
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage

    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")
        print("-- " + self.moves[3] + " --")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")


class Game:
    def __init__(self):
        self.pykemon_elements = ["FIRE", "WATER", "GRASS"]
        self.pykemon_names = ['Chewdie', 'Spatol', 'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot',
                                'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        self.battles_won = 0

    def create_pykemon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        element = self.pykemon_elements[random.randint(0, len(self.pykemon_elements)-1)]
        name = self.pykemon_names[random.randint(0, len(self.pykemon_names) - 1)]
        if element == "FIRE":
            pykemon = Fire(name, element, health, speed)
        elif element == "WATER":
            pykemon = Water(name, element, health, speed)
        else:
            pykemon = Grass(name, element, health, speed)

        return pykemon

    def choose_pykemon(self):
        starters = []
        while len(starters) < 3:
            pykemon = self.create_pykemon()
            valid_pykemon = True
            for starter in starters:
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False
            if valid_pykemon:
                starters.append(pykemon)

        for starter in starters:
            starter.show_stats()
            starter.move_info()

        print("\nProfessor Eramo presents you with three Pykemon: ")
        print("(1) - " + starters[0].name)
        print("(2) - " + starters[1].name)
        print("(3) - " + starters[2].name)
        choice = int(input("Which Pykemon would you like to choose: "))
        pykemon = starters[choice - 1]
        return pykemon

    def get_attack(self, pykemon):
        print("\nWhat would you like to do...")
        print("(1) - " + pykemon.moves[0])
        print("(2) - " + pykemon.moves[1])
        print("(3) - " + pykemon.moves[2])
        print("(4) - " + pykemon.moves[3])
        choice = int(input("Please enter your move choice: "))
        print()
        print("-----------------------------------------------------------------------------")
        return choice

    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)
        computer.faint()

    def computer_attack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        player.faint()

    def battle(self, player, computer):
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)


print("Welcome to Pykemon!")
print("Can you become the worlds greatest Pykemon Trainer???")
print("\nDon't worry! Prof Eramo is here to help you on your quest.")
print("He would like to gift you your first Pykemon!")
print("Here are three potential Pykemon partners.")
input("Press Enter to choose your Pykemon!")

playing = True
while playing:
    game = Game()
    player = game.choose_pykemon()
    print("\nCongratulations Trainer, you have chosen " + player.name + "!")
    input("\nYour journey with " + player.name + " begins now...Press Enter!")
    while player.is_alive:
        computer = game.create_pykemon()
        print("\nOH NO! A wild " + computer.name + " has approached!")
        computer.show_stats()

        while computer.is_alive and player.is_alive:
            game.battle(player, computer)

            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()
                print("-----------------------------------------------------------------------------")

        if player.is_alive:
            game.battles_won += 1

    print("\nPoor " + player.name + " has fainted...")
    print("But not before defeating " + str(game.battles_won) + " Pykemon!")

    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        playing = False
        print("Thank you for playing Pykemon!")



