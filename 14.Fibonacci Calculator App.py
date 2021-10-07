# For Loops Challenge 14: Fibonacci Calculator App

print("\nWelcome to the Fibonacci Calculator App")
number = int(input("How many digits of the Fibonacci Sequence would you like to compute:  "))

fib = [1, 1]

for i in range(number-2):
    num_1 = fib[i] + fib[i+1]
    fib.append(num_1)
print("\nThe first", number, "numbers of the Fibonacci sequence are: ")
for i in fib:
    print(i)

print("\nThe corresponding Golden Ratio values are: ")
golden_ratio = []
for i in range(number-1):
    ratio = fib[i+1]/fib[i]
    golden_ratio.append(ratio)
    print(ratio)
print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")





