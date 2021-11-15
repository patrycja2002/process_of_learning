# Conditionals Challenge 18: Voter Registration App

print("Welcome to the Voter Registration App")

name = input("\nPlease enter your name: ").title()
age = int(input("Please enter your age: "))

political_parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

if age > 17:
    print("Congratulations", str(name), "! You are old enough to register to vote.")
    print("Here is a list of political parties to join.")

    for x in political_parties:
        print("\t" + x)

    chosen_party = input("What party would you like to join: ") .title() .strip()
    if chosen_party in political_parties:
        print("Congratulations", str(name),  "! You have joined the", str(chosen_party), "party!")
        if chosen_party == "Republican" or chosen_party == "Democratic":
            print("That is a major party!")
        elif chosen_party == "Independent":
            print("You are an independent person!")
        else:
            print("That is not a major party.")
    else:
        print("That is not a given party.")
else:
    print("You are not old enough to register to vote.")



