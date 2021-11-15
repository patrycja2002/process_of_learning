#Dictionaries Challenge 24: Frequency Analysis App
from collections import Counter

print("Welcome to the Frequency Analysis App")

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '|', ' ', '.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '[', ']', '{', '}', '\n', '\t']

key_phrase_1 = input("\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)
letter_count = Counter(key_phrase_1)

print("Here is the frequency analysis from key phrase 1:")
print("\t\tLetter\t\tOccurrence\t\tPercentage")
for key, volue in sorted(letter_count.items()):
    percentage = 100*volue/total_occurrences
    percentage = round(percentage, 2)
    print("\t\t", key, "\t\t\t", volue, "\t\t\t\t", percentage, "%")

ordered_letter_count = letter_count.most_common()

key_phrase_1_order_letters = []
for x in ordered_letter_count:
    key_phrase_1_order_letters.append(x[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_order_letters:
    print(letter, end='')

key_phrase_2 = input("\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences = len(key_phrase_2)
letter_count = Counter(key_phrase_2)

print("Here is the frequency analysis from key phrase 1:")
print("\t\tLetter\t\tOccurrence\t\tPercentage")
for key, volue in sorted(letter_count.items()):
    percentage = 100*volue/total_occurrences
    percentage = round(percentage, 2)
    print("\t\t", key, "\t\t\t", str(volue), "\t\t\t\t", str(percentage), "%")

ordered_letter_count = letter_count.most_common()

key_phrase_2_order_letters = []
for x in ordered_letter_count:
    key_phrase_2_order_letters.append(x[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_order_letters:
    print(letter, end='')
