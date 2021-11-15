# For Loops Challenge 11: Binary Hexadecimal Converter App

print("Welcome to the Binary/Hexadecimal Converter App")

max_value = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists....complete!")

print("\nUsing slices, we will now show a portion of each list.")
low_range = int(input("What decimal number would you like to start at: "))
upp_range = int(input("What decimal number would you like to stop at:"))

print("\nDecimal values from", low_range, "to", upp_range)
for num in decimal[low_range-1 : upp_range]:
    print(num)

print("\nBinary values from", low_range, "to", upp_range)
for num in binary[low_range-1 : upp_range]:
    print(num)

print("\nHexadecimal values from", low_range, "to", upp_range)
for num in hexadecimal[low_range-1 : upp_range]:
    print(num)

print("Press Enter to see all values from 1 to", max_value)
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))

