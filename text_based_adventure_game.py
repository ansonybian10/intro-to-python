print("THE HIDDEN TREASURE")
print("Find the hidden treasure before it's too late!")

name = input("What is your name? ").strip().upper()

inventory = []

player = {
    "health": 20,
    "gold": 0
}

print(f"\nWelcome, {name}!")
print(f"Health: {player['health']}")

choice1 = input("\nYou stand at a fork in the road. Would you like to go to the forest or the cave? ").strip().lower()

if choice1 == "forest":
    print("\nYou walk into the dark, ominous forest.")
    locations = ["river", "cabin"]
    print(f"You discover a {locations[0]} and an old {locations[1]}.")

    choice2 = input("Do you search the cabin or follow the river? ").strip().lower()

    if choice2 == "cabin":
        print("\nYou find a golden key!")
        inventory.append("Golden Key")
    elif choice2 == "river":
        print("\nA wild wolf attacks you!")
        player["health"] -= 10
    else:
        print("\nYou get lost.")
        player["health"] = 0

elif choice1 == "cave":
    print("\nYou enter a cold cave.")
    print("You find a chest.")
    inventory.append("Golden Key")

else:
    print("\nYou wander into the wilderness.")
    player["health"] = 0

if player["health"] > 0:
    choice3 = input("\nA treasure door blocks your path. OPEN it? (yes/no) ").strip().lower()

    if choice3 == "yes":
        if "Golden Key" in inventory:
            player["gold"] = 10000
            print(f"\nCongratulations, {name}!")
            print(f"You unlocked the treasure and found {player['gold']} gold!")
            print(f"Inventory: {inventory}")
            print("YOU WIN!")
        else:
            print("\nThe door is locked.")
            print("YOU LOSE!")
    else:
        print("\nYou leave the treasure behind.")
        print("YOU LOSE!")
else:
    print("\nYour adventure has ended.")
    print("YOU LOSE!")