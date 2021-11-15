# Basic Data Types Challenge 4:  Right Triangle Solver App
import math
print("Welcome to the Right Triangle Solver App")

side_a = float(input("\nWhat is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))

side_c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
side_c = round(side_c, 3)

area = 0.5*(side_b * side_a)
area = round(area, 3)

print("\nFor a triangle with legs of " + str(side_a) + " and " + str(side_b) + " the hypotenuse is " + str(side_c) + ".")
print("For a triangle with legs of " + str(side_a) + " and " + str(side_b) + " the area is " + str(area) + ".")
