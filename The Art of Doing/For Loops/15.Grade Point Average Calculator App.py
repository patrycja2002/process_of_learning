# For Loops Challenge 15:  Grade Point Average Calculator App

print("Welcome to the Average Calculator App")
name = input("What is your name:  ").title()
number = int(input("How many grades would you like to enter: "))
grades = []
for i in range(number):
    grades.append(int(input("Enter grade: ")))

grades.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for i in grades:
    print("\t", i)

average = sum(grades)/len(grades)
average = round(average, 2)
print("\n", str(name), "'s New Grade Summary:")
print("\tTotal Number of Grades: ", len(grades))
print("\tHighest Grade: ", max(grades))
print("\tLowest Grade: ", min(grades))
print("\tAverage: ", average)

desired_average = float(input("\nWhat is your desired average:  "))
grade_req = desired_average*(len(grades)+1) - sum(grades)
grade_req = round(grade_req, 2)

print("\nGood luck " + name + "!")
print("You will need to get a ", grade_req, " on your next assignment to earn a ", desired_average, " average.")
print("Lets see what your average could have been if you did better/worse on an assignment.")

new_grades = grades[:]
change_grade = int(input("What grade would you like to change:  "))
new_grades.remove(change_grade)
new_grade = int(input("What grade would you like to change " + str(change_grade) + " to: "))
new_grades.append(new_grade)

new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest:")
for i in new_grades:
    print("\t", i)

new_average = sum(new_grades)/len(new_grades)
new_average = round(new_average, 2)
print("\n", str(name), "'s New Grade Summary:")
print("\tTotal Number of Grades: ", len(new_grades))
print("\tHighest Grade: ", max(new_grades))
print("\tLowest Grade: ", min(new_grades))
print("\tAverage: ", new_average)

ave_change = new_average - average
ave_change = round(ave_change, 2)
print("\nYour new average would be a ", new_average, " compared to your real average of", average, "!")
print("That is a change of", ave_change, "points!")
print("Too bad your original grades are still the same! ")
print(grades)
print("You should go ask for extra credit!")
