# Basic Data Types Challenge 1:  Letter Counter App

print("Welcome to the Letter Counter App")
name = input("What is your name:").title()
print("Hello, " + name + "!")

print("I will count the number of times that a specific letter occurs in a message.")
message = input("Please enter a message: ") .lower()
letter = input("Which letter would you like to count the occurrences of: ") .lower()

letter_count=message.count(letter)
print(name, "your message has "+str(letter_count)+"'s in it.")
