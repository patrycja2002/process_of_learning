# Dictionaries Challenge 23: Yes or No Polling App

print("Welcome to the Yes or No Issue Polling App")

issue = input("\nWhat is the yes or no issue you will be voting on today: ")
v_number = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

yes = 0
no = 0

results = {}

for x in range(v_number):
    name = input("\nEnter your full name: ").title()
    if name in results:
        print("Sorry, it seems that someone with that name has already voted. ")
    else:
        print("Here is our issue: " + issue)
        choice = input("What do you think...yes or no: ").lower().strip()
        if choice == "yes" or choice == "y":
            choice = "yes"
            yes += 1
        elif choice == "no" or choice == "n":
            choice= "no"
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
        results[name] = choice
        print("Thank you " + name + "! Your vote of " + results[name] + " has been recorded.")

all_votes = len(results.keys())
print("\nThe following 3 people voted:")
for key in results:
    print(key)

print("\nOn the following issue: ", issue)
if yes > no:
    print("Yes wins!", yes, "votes to", no)
elif no > yes:
    print("No wins!", no, "votes to", yes)
else:
    print("It was a tie!", yes, "votes to", no)

correct_password = input("\nTo see the voting results enter the admin password: ")
if correct_password == password:
    for key, volue in results.items():
        print("Voter: ", key, "\t\tVote", volue)
else:
    print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Yes or No Issue Polling App.")
