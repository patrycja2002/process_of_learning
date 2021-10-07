# For Loops Challenge 13: Factorial Calculator App
import math

print("Welcome to the Factorial Calculator App")

number = int(input("What number would you like to compute the factorial of? "))

print(number,  "!=", end="")
for i in range(1, number):
    print(i, end="*")
print(number)

print("\nHere is the result from the math library:")
fact = math.factorial(number)
print("The factorial of", number, "is", fact, "!")


fact = 1
for i in range(1, number+1):
    fact = fact*i
print("\nHere is the result from my own algorithm:")
print("The factorial of", number, "is", fact, "!")

print("It is shown twice that", number, "! =", fact, "  (with excitemen)")



