# Dictionaries Challenge 22: Database Admin Program

print("Welcome to the Database Admin Program")

log_on_information = {
    "mooman74" : "alskes145",
    "meramo19" : "kehns010101",
    "nickyD" : "world1star",
    "george2" : "booo3oha",
    "admin00" : "admin1234"
}

username = input("Enter your username: ")
if username in log_on_information.keys():
    password = input("Enter your password: ")
    if password in log_on_information.values():
        print("\nHello " + username + "! You are logged in!")
        if username == "admin00":
            print("\nHere is the current user database: ")
            for key, volue in log_on_information.items():
                print("Username: " +key, "\t\tPassword: " + volue)
        else:
            change_password = input("Would you like to change your password:" ).lower().strip()
            if change_password == "yes":
                new_password = input("What would you like your new password to be: ")
                if len (new_password ) >= 8:
                    log_on_information[username] = new_password
                else:
                    print(new_password + " is not the minimum eight characters.")
                print("\n" + username + " your password is " + log_on_information[username] + ".")
            else:
                print("\nThank you, goodbye.")
    else:
        print("Password incorrect!")
else:
    print("Username not in database, goodbye.")
