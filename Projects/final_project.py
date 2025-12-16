# MR 2nd Final Project
import random
import time
import sys
# function for printing the text slow enough to read
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

# functions for displaying the status
def display_team_status():
    print(f"\n--- Current Team ({len(team)}/{TEAM_NEEDED}) ---")
    if not team:
        print("No teammates recruited yet.")
    else:
        for member in team:
            print(f"- {member}")

# challenge/combat function to recruit the player
def recruit_lebron_challenge():
    print_slow("LeBron challenges you to a 1v1 to break the glitch!")
    if combat("Glitch LeBron", 60, 15):
        team.append("LeBron James")
        player["skill"] += 5
        print_slow("LeBron: 'Thanks for the assist! Let's win this.'")
# Introduction function
def intro():
    # welcoming the player and asking if they want to play
    print_slow("Welcome to Serververse Showdown!")
    print_slow("The game has been hacked.")
    print_slow("the players are missing.")
    print_slow("it's up to you to assemble the ultimate team and reclaim the court.'")
    print_slow("Ready to play for a chance at freedom?")
    
    choice = input("> ").lower().strip()
    # if statement to go to the next action
    if "yes" in choice:
        earth()
    elif "no" in choice:
        print("okay, Thank you.")
    else:
        print_slow("Invalid action. Please type 'yes' or 'no'.")
        intro()

# function to travel between worlds
def travel_options():
    while True:
        print("\nTravel Menu")
        print("1. Earth")
        print("2. DC World")
        print("3. Mad Max")
        print("4. Hogwarts")
        print("5. Wizard of Oz")
        print("6. Casablanca") 
        print("7. Thundera")
        print("8. Serververse")
        print("9. Back")

        choice = input("> ")

        if choice == "1":
            earth()
        elif choice == "2":
            dc_world()
        elif choice == "3":
            mad_max()
        elif choice == "4":
            hogwarts()
        elif choice == "5":
            oz()
        elif choice == "6":
            print("Casablanca is currently locked.") # Added placeholder
        elif choice == "7":
            thundera()
        elif choice == "8":
            serververse()
        elif choice == "9":
            break
        else:
            print("Invalid choice.")

# set the variables
player = {
    "health": 100,
    "strength": 5,
    "speed": 5,
    "skill": 5
}

inventory = []
team = []
defeated = []
TEAM_NEEDED = 5

# FUNCTIONS for each room/world
def show_stats():
    print("\nStats:")
    for stat in player:
        print(stat, player[stat])
    print("Inventory:", inventory)
    print("Team:", team)

def combat(enemy, hp, power):
    print("\nBasketball showdown against", enemy)

    while hp > 0 and player["health"] > 0:
        print("\n1. Shoot")
        print("2. Drive")
        print("3. Play Defense")
        choice = input("> ")

        if choice == "1":
            points = random.randint(5, 10) + player["skill"]
            hp -= points
            print("You hit a shot for", points, "points.")
        elif choice == "2":
            points = random.randint(4, 9) + player["speed"]
            hp -= points
            print("You drive to the hoop for", points, "points.")
        elif choice == "3":
            block = random.randint(2, 5)
            print("You play good defense.")
            power -= block
            if power < 1:
                power = 1
        else:
            print("Invalid play.")

        if hp > 0:
            enemy_points = random.randint(5, power)
            player["health"] -= enemy_points
            print(enemy, "scores", enemy_points, "points.")

    if player["health"] <= 0:
        print("You lost the game.")
        # Reset health for next try
        player["health"] = 100 
        return False

    print("You won the game against", enemy)
    defeated.append(enemy)
    return True

def earth():
    print_slow("\nYou are on Earth.")
    while True:
        choice = input("\nWhat do you do? (explore/team/travel/stats/quit)> ").lower().strip()

        if choice == "explore":
            print_slow("You hear a massive dribbling sound from the main court.")
            print_slow("It's LeBron James, but he's hypnotized by a glitch-ball!")
            recruit_lebron_challenge()
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        elif choice == "stats":
            show_stats()
        elif choice == "train": 
            player["strength"] += 1
            player["health"] += 5
            print("You trained and improved.")
        elif choice == "quit":
            sys.exit()
        else:
            print("Invalid action.")

def dc_world():
    print_slow("\nDC World")
    while True:
        choice = input("What do you do? (explore/team/travel)> ").lower().strip()

        if choice == "explore":
            if "Bugs Bunny" not in team:
                if "Joker Bot" not in defeated:
                    if combat("Joker Bot", 40, 10):
                        team.append("Bugs Bunny")
                        player["skill"] += 1
                        print("Bugs Bunny joined your team.")
                else:
                    print("The Joker Bot is already defeated.")
            else:
                print("Nothing left to do here.")
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        else:
            print("Invalid action.")

def mad_max():
    print_slow("\nMad Max Universe")
    while True:
        choice = input("What do you do? (explore/team/travel)> ").lower().strip()

        if choice == "explore":
            if "Daffy Duck" not in team:
                if "War Rig" not in defeated:
                    if combat("War Rig", 50, 12):
                        team.append("Daffy Duck")
                        player["strength"] += 1
                        print("Daffy Duck joined your team.")
            else:
                print("The Wasteland is quiet.")
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        else:
            print("Invalid action.")

def hogwarts():
    print_slow("\nHogwarts")
    while True:
        choice = input("What do you do? (explore/team/travel)> ").lower().strip()

        if choice == "explore":
            if "Magic Wand" not in inventory:
                inventory.append("Magic Wand")
                player["skill"] += 2
                print("You found a Magic Wand.")
            else:
                print("You already explored here.")
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        else:
            print("Invalid action.")

def oz():
    print_slow("\nWizard of Oz")
    while True:
        choice = input("What do you do? (explore/team/travel)> ").lower().strip()

        if choice == "explore":
            if "Lola Bunny" not in team:
                print_slow("Lola Bunny is practicing her jump shot!")
                if combat("Wicked Witch Bot", 45, 12):
                    team.append("Lola Bunny")
                    print("Lola Bunny joined the team!")
            else:
                print("The Yellow Brick Road is clear.")
        elif choice == "team":
            display_team_status()
        elif choice == "travel":
            travel_options()
            break
        else:
            print("Invalid action.")

def thundera():
    print_slow("\nThundera")
    # useless world
    print("This world seems empty for now.")
    travel_options()

def serververse():
    print_slow("\nThe Serververse Core")
    if len(team) < 3:
        print_slow("Al-G Rhythm laughs: 'You don't have enough players!'")
    else:
        print_slow("The final game begins!")
        if combat("Al-G Rhythm", 100, 20):
            print_slow("You won the Serververse Showdown and saved your team!")
            sys.exit()

# Start the game again if they want to play again
if __name__ == "__main__":
    intro()# calling the function to restart the game