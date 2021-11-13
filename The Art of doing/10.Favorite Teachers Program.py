# Lists Challenge 10:  Favorite Teachers Program

print("\nWelcome to the Favorite Teachers Program ")
fav_teachers = []
teacher = input("\nWho is your first favorite teacher: ").title()
fav_teachers.append(teacher)
teacher = input("Who is your second favorite teacher: ").title()
fav_teachers.append(teacher)
teacher = input("Who is your third favorite teacher:  ").title()
fav_teachers.append(teacher)
teacher = input("Who is your fourth favorite teacher:  ").title()
fav_teachers.append(teacher)

print("\nYour favorite teachers ranked are:", fav_teachers)
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: ", str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: ", fav_teachers[0], "and", fav_teachers[1])
print("Your next two favorite teachers are: ", fav_teachers[2], "and", fav_teachers[3])
print("Your last favorite teacher is: ", fav_teachers[3])
print("You have a total of", len(fav_teachers), " favorite teachers.")

new_teacher = input("\nOops, " + fav_teachers[0] + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title()

fav_teachers.insert(0, new_teacher)

print("\nYour favorite teachers ranked are:", fav_teachers)
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: ", str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: ", fav_teachers[0], "and", fav_teachers[1])
print("Your next two favorite teachers are: ", fav_teachers[2], "and", fav_teachers[3])
print("Your last favorite teacher is: ", fav_teachers[4])
print("You have a total of", len(fav_teachers), " favorite teachers.")

fav_teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from you list:" ).title())

print("\nYour favorite teachers ranked are:", fav_teachers)
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: ", str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: ", fav_teachers[0], "and", fav_teachers[1])
print("Your next two favorite teachers are: ", fav_teachers[2], "and", fav_teachers[3])
print("Your last favorite teacher is: ", fav_teachers[3])
print("You have a total of", len(fav_teachers), " favorite teachers.")





