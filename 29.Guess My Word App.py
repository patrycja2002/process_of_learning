# While Loops Challenge 29: Guess My Word App
import random

print("Welcome to the Guess My Word App")

game_dict = {
    "sports": ['basketball', 'baseball', 'soccer', 'football', 'tennis', 'curling'],
    "colors": ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
    "fruits": ['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
    "classes": ['english', 'history', 'science', 'mathematics', 'art', 'health'],
}

game_keys = []

for key in game_dict.keys():
    game_keys.append(key)

running = True
while running:
    game_category = game_keys[random.randint(0, len(game_keys)-1)]
    game_word = game_dict[game_category][random.randint(0, len(game_dict[game_category])-1)]

    blank_word = []
    for letter in game_word:
        blank_word.append("-")

    print("Guess a " + str(len(game_word)) + " letter word from the following category: " + game_category.title())

    guess = " "
    guess_count = 0

    while guess != game_word:
        print(" ".join(blank_word))
        guess = input("Enter your guess: ").lower()
        guess_count += 1

        if guess == game_word:
            print("Correct! You guessed the word in", str(guess_count), "guesses.")
            break

        else:
            print("That is not correct. Let us reveal a letter to help you!")

            playing = True
            while playing:
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    playing = False

    choice = input("Would you like to play again (y/n): ")
    if choice != "y":
        running = False
        print("\nThank you for playing our game.")
