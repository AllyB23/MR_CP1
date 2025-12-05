import time
import sys

# Function to print text with a slight delay for dramatic effect
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

# The game introduction and starting point
def intro():
    print_slow("Welcome to 'The Mystic Cave'!")
    print_slow("You are an adventurer seeking a fabled treasure.")
    print_slow("You stand before the dark entrance of a mountain cave.")
    print_slow("A worn sign reads: 'Only the brave or the foolish enter here.'")
    print_slow("Do you [enter] the cave or [turn back]?")
    
    choice = input("> ").lower().strip()
    
    if "enter" in choice:
        cave_entrance()
    elif "turn" in choice or "back" in choice:
        turn_back()
    else:
        print_slow("Invalid action. Please type 'enter' or 'turn back'.")
        intro()

# The end condition for turning back
def turn_back():
    print_slow("You decide the treasure isn't worth the risk and head home.")
    print_slow("You live a long, safe, and slightly dull life. Game Over.")

# First room of the adventure
def cave_entrance():
    print_slow("\nYou step into the darkness. The air is damp and cold.")
    print_slow("You light a torch. The cave splits into two paths: [left] or [right].")
    
    choice = input("> ").lower().strip()

    if "left" in choice:
        left_path()
    elif "right" in choice:
        right_path()
    else:
        print_slow("Invalid action. Please type 'left' or 'right'.")
        cave_entrance()

# The left path leads to a trap/death
def left_path():
    print_slow("\nYou follow the left path. Suddenly, the ground gives way beneath you!")
    print_slow("You fall into a pit of spikes. Your adventure ends here. Game Over.")
    
# The right path leads to a challenge
def right_path():
    print_slow("\nYou proceed down the right path. It leads to a large chamber with a pedestal.")
    print_slow("On the pedestal sits a glowing crystal. A large bear guards it, but is currently asleep.")
    print_slow("Do you try to [sneak] past the bear, or [fight] it?")
    
    choice = input("> ").lower().strip()

    if "sneak" in choice:
        sneak_past()
    elif "fight" in choice:
        fight_bear()
    else:
        print_slow("Invalid action. Please type 'sneak' or 'fight'.")
        right_path()

# Sneaking past the bear (win condition)
def sneak_past():
    print_slow("\nYou silently creep along the wall, heart pounding.")
    print_slow("The bear snorts in its sleep but doesn't wake.")
    print_slow("You grab the crystal and escape the cave! You Win!")

# Fighting the bear (death condition)
def fight_bear():
    print_slow("\nBravely, you charge the bear. It wakes up with a roar.")
    print_slow("You are no match for its fury. The bear defeats you. Game Over.")

# This line starts the game when the script is run
if __name__ == "__main__":
    intro()