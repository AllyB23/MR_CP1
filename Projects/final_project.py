# MR 2nd Final Project
import random
import time
import sys
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def intro():
    print_slow("Welcome to Serververse Showdown!")
    print_slow("The game has been hacked.")
    print_slow("the players are missing.")
    print_slow("it's up to you to assemble the ultimate team and reclaim the court.'")
    print_slow("Ready to play for a chance at freedom?")
    
    choice = input("> ").lower().strip()
    
    if "yes" in choice:
        earth()
    elif "no" in choice:
        print("okay, Thank you.")
    else:
        print_slow("Invalid action. Please type 'enter' or 'turn back'.")
        intro()

"""#choice = input("Welcome to Serververse Showdown.\n The game has been hacked, the players are missing,\n and it's up to you to assemble the ultimate team and reclaim the court.\n Ready to play for a chance at freedom?\n").lower()

#if choice == ('yes'):
    print("okay! let's go!")
    print("You will be traveling to different worlds\n and going to recruit the players to play the ultimate game of basketball!")
    print("You have to save the toons from the other worlds\n and get back to your family!")
#elif choice ==("no"):
    print("okay, thank you.")
else:
    print("Please enter a valid option.")"""

"""player_stats: {
basketball_IQ: 5, 
stamina = 5,
looney_abilities = 5,
strength = 5,
speed = 5,
shooting = 5}"""""

# VARAIABLES/ITEMS/CHARACTERS
lola_bunny = True
bugs_bunny = True
Tweety = True
Granny = True
lebron_james = True
daffy_duck = True
porky_pig = True
the_brow = True
arachneka = True
the_white_mamba = True
wet_fire = True
chronos = True


#if characters == "LeBron James"():
   # pass

def earth():
    print("You are currently on earth.")
    pass
def DC_World():
    print("You are currently in DC World.")
    pass
def Mad_Max_universe():
    print("You are currently in Mad Max Universe.")
    pass
def Austin_powers_world():
    print("You are currently in Austin Powers World.")
    pass
def Wizard_of_oz_world():
    print("You are currently in Austin Powers world.")
    pass
def Hogwarts():
    print("You are currently in Hogwarts.")
    pass
def casablanca_world():
    print("You are currently in Casablanca world.")
    pass
def Thundera():
    print("You are currently in Thundera.")
    pass
def serververse():
    print("You currently in the serververse.")
    pass
def toon_world():
    print("You are finally here!\n It is time to play the ultimate game of basketball!")
    pass
