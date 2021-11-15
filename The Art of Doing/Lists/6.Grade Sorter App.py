# Lists Challenge 6:  Grade Sorter App

print("Welcome to the Grade Sorter App")
all_g = []
grade = int(input("\nWhat is your first grade (0-100):  "))
all_g.append(grade)
grade = int(input("What is your second grade (0-100): "))
all_g.append(grade)
grade = int(input("What is your third grade (0-100):  "))
all_g.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
all_g.append(grade)

all_g.sort()
all_g.reverse()

print("\nYour grades are: " + str(all_g))
print("\nYour grades from highest to lowest are: ", all_g)

print("The lowest two grades will now be dropped. ")

print("Removed grade: ", all_g.pop(3))
print("Removed grade: ", all_g.pop(2))
print("\nYour remaining grades are: ", all_g)
print("Nice work!  Your highest grade is a", all_g[0])

