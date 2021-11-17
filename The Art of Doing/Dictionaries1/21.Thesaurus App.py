# Dictionaries Challenge 21: Thesaurus App
import random

thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print("Welcome to the Thesaurus App!")
print("\n\nChoose a word from the thesaurus and I will give you a synonym")
print("Here are the words in the thesaurus: ")


for key in thesaurus.keys():
    print("\t-", key)

word = input("What word would you like a synonym for: ").lower().strip()

if word in thesaurus.keys():
    index = random.randint(0, 4)
    print("A synonym for " + word + " is " + thesaurus[word][index] + ".")
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

choice = input("Would you like to see the whole thesaurus (yes/no): ").lower().strip()

if choice == "yes":
    for key, values in thesaurus.items():
        print("\n" + key.title() + " synonyms are:")
        for value in values:
            print("\t-" + value)
else:
    print("\nI hope you enjoyed the program. Thank you!")
