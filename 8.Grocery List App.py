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
foods.append(food)
food = (input("Type of food to add to the grocery list:  "))
foods.append(food)
food = (input("Type of food to add to the grocery list:  "))
foods.append(food)

print("Here is your grocery list")
print(foods)
