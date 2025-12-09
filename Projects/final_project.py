# MR 2nd Final Project
import random
import time
import sys
def slow_print(text, delay=0.04): # Slightly faster default delay
    """
    Prints text character by character with a delay.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Print a final newline character after the text is complete
choice = input().lower()
def welcome_player():
    print("Hello, you will be traveling to different worlds\n and going to recruit the players to play the ultimate game of basketball!")
    time.sleep(1.5)
    print("You have to save the toons from the other worlds\n and get back to your family!")
    time.sleep(2)
choice = input("Welcome to Serververse Showdown.\n The game has been hacked, the players are missing,\n and it's up to you to assemble the ultimate team and reclaim the court.\n Ready to play for a chance at freedom?\n").lower()

print()
welcome_player()

# Use slow_print for the main intro text leading up to the prompt
slow_print("Welcome to Serververse Showdown.\n The game has been hacked, the players are missing,\n and it's up to you to assemble the ultimate team and reclaim the court.")

# Handle the input prompt slightly differently:
# 1. Print the prompt text slowly without a final newline.
# 2. Capture the input immediately after the slow print finishes.
prompt_text = "Ready to play for a chance at freedom?\n> "
# Use sys.stdout.write and flush one last time for the input prompt itself
for char in prompt_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04) # Match the typing speed

choice = input().lower()
def welcome_player():
    print("Hello, you will be traveling to different worlds\n and going to recruit the players to play the ultimate game of basketball!")
    time.sleep(1.5)
    print("You have to save the toons from the other worlds\n and get back to your family!")
    time.sleep(2)
choice = input("Welcome to Serververse Showdown.\n The game has been hacked, the players are missing,\n and it's up to you to assemble the ultimate team and reclaim the court.\n Ready to play for a chance at freedom?\n").lower()

if choice == ('yes'):
    print("okay! let's go!")

    welcome_player()

elif choice ==("no"):
    print("okay, thank you.")
else:
    print("Please enter a valid option.")
#def print_slow(text):
"""player_stats: {
basketball_IQ: 5, 
stamina = 5,
looney_abilities = 5,
strength = 5,
speed = 5,
shooting = 5}"""""

#characters  = input(print("What character would you like to be?"({})))

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
