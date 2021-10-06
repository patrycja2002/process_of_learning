# Lists Challenge 8:  Grocery List App
import datetime
print("\nWelcome to the Grocery List App.")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print("Current Date and Time: ",  month, "/", day,"\t", hour, ":", minute)
foods = ["Meat", "Cheese"]
print("You currently have ", foods[0], "and", foods[1], "in your list.")


food = (input("\nType of food to add to the grocery list:  "))
foods.append(food.title())
food = (input("Type of food to add to the grocery list:  "))
foods.append(food.title())
food = (input("Type of food to add to the grocery list:  "))
foods.append(food.title())

print("\Here is your grocery list")
print(foods)

foods.sort()
print("Here is your grocery list sorted:")
print(foods)

print("\nSimulating grocery shopping... ")

print("\nCurrent grocery list:", len(foods), "items")
print(foods)
b_f = input("What food did you just buy: ") .title()
foods.remove(b_f)
print("Removing",  b_f, " from list...")

print("\nCurrent grocery list:", len(foods), "items")
print(foods)
b_f = input("What food did you just buy: ") .title()
foods.remove(b_f)
print("Removing",  b_f, " from list...")

print("\nCurrent grocery list:", len(foods), "items")
print(foods)
b_f = input("What food did you just buy: ") .title()
foods.remove(b_f)
print("Removing",  b_f, " from list...")

print("\nCurrent grocery list:", len(foods), "items")
print(foods)

no_food = foods.pop()
print("\nSorry, the store is out of " + no_food + ".")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remains on your grocery list: ")
print(foods)


