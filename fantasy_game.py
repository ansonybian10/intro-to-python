level = int(input("What is your player level? "))
if level < 10:
    print("Level up!")
else:
    weapon = input("Do you have a weapon? (yes/no) ")
    if weapon.lower() == "no":
        print("You need a weapon to fight!")
    else:
        health = int(input("What is your health? "))
        if health < 50:
            print("You need to heal up!")
        else:
            print("You are ready to fight!") 