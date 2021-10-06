# Lists Challenge 9:  Basketball Roster Program

print("\nWelcome to the Basketball Roster Program ")

team = []
player = input("\nWho is your point guard:  ").title()
team.append(player)
player = input("Who is your shooting guard:  ").title()
team.append(player)
player = input("Who is your small forward: ").title()
team.append(player)
player = input("Who is your power forward:  ").title()
team.append(player)
player = input("Who is your center:  ").title()
team.append(player)

print("\n\tYour starting", len(team), "for the upcoming basketball season ")
print("\t\tPoint Guard: \t\t", team[0])
print("\t\tShooting Guard: \t", team[1])
print("\t\tSmall Forward: \t\t", team[2])
print("\t\tPower Forward: \t\t", team[3])
print("\t\tCenter: \t\t\t", team[4])

injured_player = team.pop(2)

print("\nOh no,", injured_player, "is injured")
print("Your roster only has ", len(team), "players.")

added_player = input("Who will take " + injured_player + "'s spot: ") .title()

team.insert(2, added_player)
print("\n\tYour starting", len(team), "for the upcoming basketball season ")
print("\t\tPoint Guard: \t\t", team[0])
print("\t\tShooting Guard: \t", team[1])
print("\t\tSmall Forward: \t\t", team[2])
print("\t\tPower Forward: \t\t", team[3])
print("\t\tCenter: \t\t\t", team[4])

print("\nGood luck ", team[2], " you will do great! ")
print("Your roster now has ", len(team), " players.")




