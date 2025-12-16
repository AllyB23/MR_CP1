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
# FUNCTIONS
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
        return False

    print("You won the game against", enemy)
    defeated.append(enemy)
    return True

def earth():
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
    print("\nYou are on Earth.")
    print("1. Train")
    print("2. Travel")
    print("3. Stats")
    print("4. Quit")

    choice = input("> ")

    if choice == "1":
        player["strength"] += 1
        player["health"] += 5
        print("You trained and improved.")
    elif choice == "2":
        travel()
    elif choice == "3":
        show_stats()
    elif choice == "4":
        quit()
    else:
        print("Invalid choice.")

def dc_world():
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
    print("\nDC World")
    if "Bugs Bunny" not in team:
        if "Joker Bot" not in defeated:
            if combat("Joker Bot", 40, 10):
                team.append("Bugs Bunny")
                player["skill"] += 1
                print("Bugs Bunny joined your team.")
    else:
        print("Nothing left to do here.")

def mad_max():
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
    print("\nMad Max Universe")
    if "Daffy Duck" not in team:
        if "War Rig" not in defeated:
            if combat("War Rig", 50, 12):
                team.append("Daffy Duck")
                player["strength"] += 1
                print("Daffy Duck joined your team.")

def hogwarts():
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
    print("\nHogwarts")
    if "Magic Wand" not in inventory:
        inventory.append("Magic Wand")
        player["skill"] += 2
        print("You found a Magic Wand.")
    else:
        print("You already explored here.")

def oz():
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
    print("\nWizard of Oz")
    if "Lola Bunny" not in team:
        team.append("Lola Bunny")
        player["speed"] += 1
        print("Lola Bunny joined your team.")

def casablanca():
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
    print("\nCasablanca")
    player["health"] += 10
    print("You rest and recover stamina.")

def thundera():
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
    print("\nThundera")
    if "Porky Pig" not in team:
        team.append("Porky Pig")
        player["strength"] += 1
        print("Porky Pig joined your team.")

def serververse():
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
    print("\nSerververse")
    if len(team) < TEAM_NEEDED:
        print("You need more teammates before the final game.")
        return

    if "Goon Squad" not in defeated:
        if combat("Goon Squad", 120, 15):
            print("You won the ultimate basketball game.")
            print("Tune World is saved.")
            play_again()

def travel():
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
            casablanca()
        elif choice == "7":
            thundera()
        elif choice == "8":
            serververse()
        elif choice == "9":
            break
        else:
            print("Invalid choice.")

def play_again():
    choice = input("Play again? (yes/no) ").lower()
    if choice == "yes":
        main()
    else:
        quit()

def main():
    print("Welcome to Serververse Showdown.")
    print("The game has been hacked.")
    print("The players are missing.")

    start = input("Ready to play? (yes/no) ").lower()

    if start == "yes":
        while True:
            earth()
    else:
        print("Goodbye.")

main()
