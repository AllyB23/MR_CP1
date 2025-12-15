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

choice = input("Welcome to Serververse Showdown.\n The game has been hacked, the players are missing,\n and it's up to you to assemble the ultimate team and reclaim the court.\n Ready to play for a chance at freedom?\n").lower()

if choice == ('yes'):
    print_slow("okay! let's go!")
    print_slow("You will be traveling to different worlds\n and going to recruit the players to play the ultimate game of basketball!")
    print_slow("You have to save the toons from the other worlds\n and get back to your family!")
#elif choice ==("no"):
    print_slow("okay, thank you.")
else:
    print_slow("Please enter a valid option.")

"""player_stats: {
basketball_IQ: 5, 
stamina = 5,
looney_abilities = 5,
strength = 5,
speed = 5,
shooting = 5}"""""
recruited_team = []
team_size_needed = 5
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

player_check = input("Would you like to check if there is any players in this world?")
while True:
        choice = input("What do you do? (explore/team/travel)> ").lower().strip()

        if choice == "explore":
            print_slow("You hear a massive dribbling sound from the main court.")
            print_slow("It's LeBron James, but he's hypnotized by a glitch-ball!")
            recruit_lebron_challenge()
            break # Exit the while loop once the challenge starts
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        else:
            print("Invalid action. Options are: explore, team, travel.")
        def recruit_lebron_challenge():
            print("\nLeBron challenges you to a 3-point contest to break the spell!")
            print("You need to make 3 out of 5 shots.")
    
shots_made = 0
for i in range(1, 6):
        print_slow(f"--- Shot {i}/5 ---")
        guess = input("Enter 'shoot' to take the shot: ").lower().strip()
        if guess == 'shoot':
            # 60% chance to make the shot
            if random.randint(1, 10) <= 6: 
                print_slow("SWISH! You make the shot.")
                shots_made += 1
            else:
                print_slow("Clank! Off the rim.")
        else:
            print_slow("You fumbled the ball! Missed shot.")

            print_slow(f"\nContest Over! You made {shots_made} shots.")

if shots_made >= 3:
        print_slow("You won the contest! The glitch ball shatters and LeBron snaps out of his trance.")
        print_slow("LeBron James says: 'I'm in. Let's go save the Serververse!'")
        recruited_team.append("LeBron James")
        display_team_status()
        travel_options()
else:
        print_slow("You lost the contest. LeBron dribbles away.")
        print_slow("You must try again or travel elsewhere to build your skills.")
        # Send player back to Earth menu
        earth()
def travel_options():
    print_slow("\nWhere would you like to travel next?")
    print_slow("Available destinations: DC_World, Mad_Max_universe, Hogwarts, Serververse")
    
    while True:
        destination = input("Enter destination name: ").lower().replace(" ", "_").strip()

        # Check if the destination is one of your functions and call it
        if destination == "dc_world":
            DC_World()
            break
        elif destination == "mad_max_universe":
            Mad_Max_universe()
            break
        elif destination == "hogwarts":
            Hogwarts()
            break
        elif destination == "serververse":
            # This should be the final boss trigger
            serververse()
            break
        else:
            print_slow("Invalid destination. Check your spelling or try another location.")

def earth():
    print("You are currently on earth.")
    if "LeBron James" in recruited_team:
        print("LeBron is already on your team. Time to find the others!")
        travel_options()
        return

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
