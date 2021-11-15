# Conditionals Challenge 16: Shipping Accounts Program

users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
print("Welcome to the Shipping Accounts Program")

username = input("\nHello, what is your username: ") .lower()
if username in users:
    print("\nHello " + username + ". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100: \t\t\t$5.10 each")
    print("Shipping orders 100 to 500: \t\t$5.00 each")
    print("Shipping orders 500 to 1000: \t\t$4.95 each")
    print("Shipping orders over 1000: \t\t\t$4.80 each")

    items = int(input("\nHow many items would you like to ship: "))
    if items < 100:
        cost = 5.10
    elif items < 500:
        cost = 5.00
    elif items < 1000:
        cost = 4.95
    else:
        cost = 4.80

    bill = items*cost
    bill = round(bill, 2)
    print("To ship", items, "items it will cost you $", bill, "at $", cost, "per item." )

    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
        print("Okay. Shipping your ", items, " items.")
    else:
        print("Okay, no order is being placed at this time.")

else:
    print("Sorry, you do not have an account with us. Goodbye.")
