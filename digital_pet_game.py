print("Welcome to the Digital Pet Game!")
print("In this game, you will take care of a digital pet and keep it happy and healthy.")
print("You can feed it, play with it, make it sleep, and take care of its needs.")
print("The goal is to keep your pet alive and healthy for as long as possible.")
print("Have fun, and good luck!")
print("First, let's create your pet!")

pet_name = input("What is the pet's name? ")
pet_type = input("What type of pet is it? (dog, cat, or dragon) ")
while pet_type.lower() not in ["dog", "cat", "dragon"]:
    print("Invalid pet type. Please choose dog, cat, or dragon.")
    pet_type = input("What type of pet is it? (dog, cat, or dragon) ")

hunger = 80
happiness = 80
health = 80
energy = 80
cleanliness = 100

print("Your pet's initial overall health is " + str(health) + ", happiness is " + str(happiness) + ", energy is " + str(energy) + ", and cleanliness is " + str(cleanliness) + ".")
print("If any of these stats reach 0, something bad happens, which is not ideal.")
if pet_type.lower() == "dog":
    emoji = "🐕"
elif pet_type.lower() == "cat":
    emoji = "🐈"
else:
    emoji = "🐉"

print(f"Your pet, named {pet_name}, is a {pet_type} and looks like this: {emoji}.")

if hunger > 100:
    hunger = 100
elif hunger < 0:
    hunger = 0

if happiness > 100:
    happiness = 100
elif happiness < 0:
    happiness = 0

if health > 100:
    health = 100
elif health < 0:
    health = 0

hunger_bar = "X" * (hunger // 10)
happiness_bar = "X" * (happiness // 10)
health_bar = "X" * (health // 10)

if happiness >= 80:
    mood = "ecstatic"
elif happiness >= 60:
    mood = "happy"
elif happiness >= 40:
    mood = "okay"
elif happiness >= 20:
    mood = "sad"
else:
    mood = "miserable"

print("Here are your current pet stats:")
print("Hunger: [" + hunger_bar + "]")
print("Happiness: [" + happiness_bar + "]")
print("Health: [" + health_bar + "]")
print("Mood: " + mood)

for turn in range(1, 6):
    print("Turn " + str(turn) + " of 5")

    hunger_bar = "X" * (hunger // 10)
    happiness_bar = "X" * (happiness // 10)
    health_bar = "X" * (health // 10)

    print("Hunger: [" + hunger_bar + "]")
    print("Happiness: [" + happiness_bar + "]")
    print("Health: [" + health_bar + "]")

    print("1. Feed")
    print("2. Play")
    print("3. Sleep")

    choice = input("What would you like to do? ")

    while choice not in ["1", "2", "3"]:
        print("That's not an option! Please enter 1, 2, or 3.")
        choice = input("What would you like to do? ")
    
    if choice == "1":
        hunger += 25
        happiness += 10
        health -= 5
        print("You decided to feed your pet!")

    elif choice == "2":
        happiness += 25
        hunger -= 15
        health += 5
        print("You decided to play with your pet!")
        if pet_type.lower() == "dog":
            happiness += 10

    else:
        health += 20
        happiness += 10
        hunger -= 10
        print("You decided to let your pet take a nap!")
        if pet_type.lower() == "cat":
            health += 10

     if hunger > 100:
        hunger = 100
    elif hunger < 0:
        hunger = 0

    if happiness > 100:
        happiness = 100
    elif happiness < 0:
        happiness = 0

    if health > 100:
        health = 100
    elif health < 0:
        health = 0

    hunger -= 10
    happiness -= 5

    if pet_type.lower() == "dragon":
        hunger -= 10

    if hunger > 100:
        hunger = 100
    elif hunger < 0:
        hunger = 0

    if happiness > 100:
        happiness = 100
    elif happiness < 0:
        happiness = 0

    if health > 100:
        health = 100
    elif health < 0:
        health = 0

    if hunger < 20:
        print("Watch out! Hunger is below 20!")

    if happiness < 20:
        print("Watch out! Happiness is below 20!")

    if health < 20:
        print("Watch out! Health is below 20!")

    if hunger == 0:
        health -= 15

        if health < 0:
            health = 0

    if health == 0:
        print("Game over! Your pet died!")
        break

