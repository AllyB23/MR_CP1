# MR 2nd combat program

print("Welcome to training! First I need to know some things about you!")
name = input("What is your name: ")
print("What class of fighter are you? ")
fighter_class = input("1:Fighter  2: Mage, or 3: Rogue\n")


number = fighter_class

if number == 1:
        print("Great, here are your stats!\n Health:30 \n Defense: 14 \n Attack: D20 \n Damage: D8 +4 \n You are being attacked by a Dire Wolf!\n You move first!\n")
elif type(fighter_class) == str:
        print("please try again. ")