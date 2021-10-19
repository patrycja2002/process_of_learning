# Conditionals Challenge 20: Rock, Paper, Scissors App
import random

print("Welcome to a game of Rock, Paper, Scissors")
rounds = int(input("\nHow many rounds would you like to play: "))

moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

for x in range(rounds):
    print("\nRound", str(x+1))
    print("Player:", str(player_score), "Computer:", str(computer_score))

    computer_index = random.randint(0, 2)
    computer_choice = moves[computer_index]

    player_choice = input("Time to pick...rock, paper, scissors:").lower().strip()
    if player_choice in moves:
        print("\tComputer:", computer_choice)
        print("\tPayer:", player_choice)
        if computer_choice == "rock" and player_choice == "rock":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif computer_choice == "paper" and player_choice == "rock":
            winner = "computer"
            phrase = "Paper covers rock!"
        elif computer_choice == "scissors" and player_choice == "rock":
            winner = "player"
            phrase = "Rock smashes scissors!"
        elif computer_choice == "scissors" and player_choice == "scissors":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif computer_choice == "rock" and player_choice == "scissors":
            winner = "computer"
            phrase = "Rock smashes scissors!"
        elif computer_choice == "paper" and player_choice == "scissors":
            winner = "player"
            phrase = "Scissors cut paper!"
        elif computer_choice == "paper" and player_choice == "paper":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif computer_choice == "rock" and player_choice == "paper":
            winner = "player"
            phrase = "Paper covers rock!"
        elif computer_choice == "scissors" and player_choice == "paper":
            winner = "computer"
            phrase = "Scissors cut paper!"
        else:
            print("Round winner not calculated.")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'

        print("\t" + phrase)
        if winner == 'player':
            print("\tYou win round " + str(x+ 1) + ".")
            player_score += 1
        elif winner == 'computer':
            print("\tComputer wins round " + str(x + 1) + ".")
            computer_score += 1
        else:
            print("\tThis round was a tie.")
    else:
        print("That is not a valid game option!")
        print("Computer gets the point!")
        computer_score += 1
print("\nFinal Game Results", )
print("\tRounds Played:", rounds)
print("\tPlayer Score:", player_score)
print("\tComputer Score:", computer_score)
if player_score > computer_score:
    print("\tWinner: PLAYER!!!")
elif computer_score > player_score:
    print("\tWinner: Computer :-(")
else:
    print("\tThe game was a tie.")
