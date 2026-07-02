print("Welcome to the Carbon Footprint Calculator! Here, you will see how big your personal carbon footprint is.")
showers = float(input("How many showers do you take per day? "))
meals = float(input("How many meals are cooked per day? "))
meals_stove = input("What kind of stove is used to cook your meals? (gas, electric, induction) ")
transportation = float(input("How many miles per day do you travel by car? "))
transportation_type = input("What type of car do you drive? (gas, hybrid, electric) ")
lights_hours = float(input("How many hours per day are the lights in your home on? "))
lights_number = int(input("How many lights are in your home? "))
computer_hours = float(input("How many hours per day is your computer on? "))
ac = float(input("How many hours per day is your air conditioning on? "))

showers_footprint = showers * 0.9

if meals_stove == "gas":
    meals_footprint = meals * 0.45
elif meals_stove == "electric":
    meals_footprint = meals * 0.3
else:
    meals_footprint = meals * 0.18


if transportation_type == "gas":
    transportation_footprint = transportation * 0.4
elif transportation_type == "hybrid":
    transportation_footprint = transportation * 0.2
else:
    transportation_footprint = transportation * 0.1

lights_footprint = lights_hours * lights_number * 0.01
computer_footprint = computer_hours * 0.02
ac_footprint = ac * 0.15

total_footprint = (showers_footprint + meals_footprint + transportation_footprint + lights_footprint + computer_footprint + ac_footprint)

print("Showers footprint: " + str(showers_footprint))
print("Meals footprint: " + str(meals_footprint))
print("Transportation footprint: " + str(transportation_footprint))
print("Lights footprint: " + str(lights_footprint))
print("Computer footprint: " + str(computer_footprint))
print("AC footprint: " + str(ac_footprint))
print("Your total daily carbon footprint is: " + str(total_footprint) + " kg CO2")