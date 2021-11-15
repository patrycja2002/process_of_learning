# Basic Data Types Challenge 5:  Multiplication/Exponent Table App
import math
print("\nWelcome to the Multiplication/Exponent Table App")

name = input("\nWhat is your name: ") .title()
number = float(input("What number would you like to work with: "))
message = name + ", Math is cool!"

# Multiplication Table
print("\nMultiplication Table For " + str(number))
print("\n\t1.0 * " + str(number) + " = ", round(1*number, 4))
print("\t2.0 * " + str(number) + " = ", round(2*number, 4))
print("\t3.0 * " + str(number) + " = ", round(3*number, 4))
print("\t4.0 * " + str(number) + " = ", round(4*number, 4))
print("\t5.0 * " + str(number) + " = ", round(5*number, 4))
print("\t6.0 * " + str(number) + " = ", round(6*number, 4))
print("\t7.0 * " + str(number) + " = ", round(7*number, 4))
print("\t8.0 * " + str(number) + " = ", round(8*number, 4))
print("\t9.0 * " + str(number) + " = ", round(9*number, 4))

# Exponent Table
print("\nExponent Table For " + str(number))
print("\n\t1.0 ** " + str(number) + " = ", round(number**1, 4))
print("\t2.0 ** " + str(number) + " = ", round(number**2, 4))
print("\t3.0 ** " + str(number) + " = ", round(number**3, 4))
print("\t4.0 ** " + str(number) + " = ", round(number**4, 4))
print("\t5.0 ** " + str(number) + " = ", round(number**5, 4))
print("\t6.0 ** " + str(number) + " = ", round(number**6, 4))
print("\t7.0 ** " + str(number) + " = ", round(number**7, 4))
print("\t8.0 ** " + str(number) + " = ", round(number**8, 4))
print("\t9.0 ** " + str(number) + " = ", round(number**9, 4))

# Math is cool
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())






