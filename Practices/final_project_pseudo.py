# MR 2nd Final Project Pseudocode
# Import random number library
# Import time library

# We will welcome the user using a function 
# def print_slow(text):
# make print statements to welcome the user
# EXPLANATION
# Variables
# Character 
# We will make other variables that establish the stats of all the players.
# we will make a list of recruited players
# Another variable that tracks the worlds that we have traveled
# Another list for items gained
# A boolean that controls the main loop
# CHARACTERS
#Lola Bunny: {}
#Bugs Bunny: {}
#Tweety: {}
#Granny: {}
#LeBron James: {}
#Daffy Duck: {}
#Porky Pig: {}
# Sylvester_the_cat: {}
# player stats
""" player_sats: {
Basketball_IQ:5,
    Stamina/Durability:5,
    Looney_Ablilities:5,
    Strength:5,
    Speed:5,
    Shooting:5}
    """
# Items available in the game
# Items =  {
 # "Magic Basketball": False,
 #   "ACME Power Drink": False
#}
# Enemy/combat tracking so bosses don't respawn
#enemy_status = {
 #   "Al_G_Rhythm": "alive",
  #  "Goon_Defender": "alive"
#}
#IF item has NOT already been collected:
#    add item to items_collected
#    apply stat bonus if any
#ELSE:
#    print "Item already taken"
# FUNCTIONS/WORLDS
"""Earth: LeBron James(player)
DC World (Gotham city/ Metropolis): Daffy Duck(Player)
Mad Max Universe: 
Austin Powers World
Wizard of Oz World
Hogwarts(Harry Potter World)
Casablanca world
Serververse: Al-G Rythm(Villain/Antagonist)
Thundera(Thundercats universe)
Tune World: bugs bunny(character)"""
# They will have the option to go to whatever world they like from the random 3 that they are given
# IF statement to lead them to the room.
# User input to ask them what world they would like to go to
# IF statements to decide which world to travel because they only have the the option of 3 to choose from
#FUNCTION increase_stats(stat_name, amount):
#    player_stats[stat_name] += amount
#    print stat increased
# While the game is running (this is the main loop)
#Show the player three random roooms to choose from
# The game will not pick ones that have been locked out, order can be random
#ASk the player to pick one of those world or choose to quit
# if the player choose to quit us a break to exit the main loop
# When the player enters a chosen world
# Mark the world as visited (add to visited_worlds if not already there).
#if user tries to access the final boss prematurely, require conditions (e.g., must have Magic Basketball or 7 recruits).
#Functions (logical blocks you can later write as functions)
#show_welcome_message()
#choose_world() — shows 3 worlds and gets input
#enter_world(world) — handles recruitment, items, enemies
#start_combat(enemy) — full combat handling
#pick_up_item(item) — item pickup and effect
#increase_stats(source, stat, amount) — change a stat
#restart_game() — resets everything
#Lists
#player_team, visited_worlds, items_collected
"""""""
# First world of the game
# DEF Earth():
    # We will state the location of the user
    # If the character is LeBron James then they start out on earth so we will make an if statement out of the function to lead the player here
    # After that we will ask them to what world they want to to next using a user input
    # We will check earth if there is any players to recruit 
    # If there is none return False
    # IF LEBRON_JAMES_IS_AVAILABLE THEN
    # print "LeBron James is here!"
    # ADD Lebron James to team (using append)
    # print("LeBron James has joined the toon squad!")
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE
# Check: does this world have a character who is still recruitable?
# IF yes:
# Announce the character and offer to recruit them.
# If player accepts, append that character to player_team. (Change: player_team grows.)
# Possibly apply an immediate stat change (e.g., recruiting LeBron increases Shooting).
# IF no:
# Tell the player “Nothing here” or “Character already recruited.”
#Check: does the world contain an item not yet collected?
# IF yes:
# Offer item pickup.
# If player picks up the item, add it to items_collected and apply any instant stat bonus.
# IF no:
# Nothing to pick up.
# Check: is there an enemy here that’s still alive?
# IF yes:
# Trigger a combat encounter (see Combat logic).
# IF no:
# Skip combat.
# After all the above, return to the main loop (show three worlds again).
# How combat works (detailed)
# Starting combat
# Check enemy_status for this enemy.
# IF enemy_status == dead:
# Skip combat (enemy already defeated).
# ELSE:
# Begin fighting.
# Combat loop (repeat until one side is defeated)
# While both player_health > 0 AND enemy_health > 0:
# Present player action choices: Attack, Use ability, Use item, Defend/Dodge, or Run (if allowed).
# Player picks action.
# IF Attack:
# Damage to enemy = number based on player’s Strength (plus weapon bonus if any).
# Subtract damage from enemy_health.
# IF Use ability:
# Damage or effect based on Looney_Abilities (may use up stamina or a cooldown).
# Subtract damage from enemy_health or apply a special effect (stun, weaken).
# IF Use item:
# If player has that item in items_collected, apply its effect (heal, buff, extra damage).
# Remove item if it’s consumable.
# IF Defend/Dodge:
# Reduce or avoid the next enemy attack (temporary effect).
# IF Run:
# Attempt to leave combat; success depends on Speed or a random chance.
# IF run succeeds: exit combat loop and return to the world (enemy remains alive).
# IF run fails: enemy gets a free attack.
# AFTER the player action (unless enemy already died):
# Enemy responds: enemy attacks or uses ability.
# Damage to player = calculated from enemy attack minus any defend/dodge effect.
# Subtract from player_health.
# Check post-attack health:v
# IF enemy_health <= # 0:
# Mark enemy_status[evnemy] = dead (enemy won’t reappear).
# Reward player (XP,#  item drop, or stat increase).
# Exit combat loop.



# DEF DC World():
    # We will state the location of the user
    # If the character is Daffy Duck then the player will come to this room/world and choose who to go recruit next
    # If there is none return False
    # IF_LOLA_BUNNY_IS_AVIALBLE_THEN
    # print "Lola Bunny is here!"
    # ADD Lola bunny to team (using append)
    # print "Lola Bunny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Lola Bunny has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE
# Check: does this world have a character who is still recruitable?
# IF yes:
# Announce the character and offer to recruit them.
# If player accepts, append that character to player_team. (Change: player_team grows.)
# Possibly apply an immediate stat change (e.g., recruiting LeBron increases Shooting).
# IF no:
# Tell the player “Nothing here” or “Character already recruited.”
#Check: does the world contain an item not yet collected?
# IF yes:
# Offer item pickup.
# If player picks up the item, add it to items_collected and apply any instant stat bonus.
# IF no:
# Nothing to pick up.
# Check: is there an enemy here that’s still alive?
# IF yes:
# Trigger a combat encounter (see Combat logic).
# IF no:
# Skip combat.
# After all the above, return to the main loop (show three worlds again).
# How combat works (detailed)
# Starting combat
# Check enemy_status for this enemy.
# IF enemy_status == dead:
# Skip combat (enemy already defeated).
# ELSE:
# Begin fighting.
# Combat loop (repeat until one side is defeated)
# While both player_health > 0 AND enemy_health > 0:
# Present player action choices: Attack, Use ability, Use item, Defend/Dodge, or Run (if allowed).
# Player picks action.
# IF Attack:
# Damage to enemy = number based on player’s Strength (plus weapon bonus if any).
# Subtract damage from enemy_health.
# IF Use ability:
# Damage or effect based on Looney_Abilities (may use up stamina or a cooldown).
# Subtract damage from enemy_health or apply a special effect (stun, weaken).
# IF Use item:
# If player has that item in items_collected, apply its effect (heal, buff, extra damage).
# Remove item if it’s consumable.
# IF Defend/Dodge:
# Reduce or avoid the next enemy attack (temporary effect).
# IF Run:
# Attempt to leave combat; success depends on Speed or a random chance.
# IF run succeeds: exit combat loop and return to the world (enemy remains alive).
# IF run fails: enemy gets a free attack.
# AFTER the player action (unless enemy already died):
# Enemy responds: enemy attacks or uses ability.
# Damage to player = calculated from enemy attack minus any defend/dodge effect.
# Subtract from player_health.
# Check post-attack health:v
# IF enemy_health <= # 0:
# Mark enemy_status[evnemy] = dead (enemy won’t reappear).
# Reward player (XP,#  item drop, or stat increase).
# Exit combat loop.
# DO THIS FOR ALL THE FUNCTIONS

# DEF Mad Max Universe():
    # We will state the location of the user
    # if the character is Bugs Bunny the player wil start out on Mad Max Universe
    # If there is none return False
    # IF BUGS_BUNNY_IS_AVAILABLE THEN
    # print "Bugs Bunny is here!"
    # ADD Bugs Bunny to team (using append)
    # print "Bugs bunny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Bugs Bunny has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Austin Powers World():
    # We will state the location of the user
    # If there is none return False
    # SYLVESTER_THE_CAT_IS_AVAILABLE THEN
    # print " Sylvester the cat is here!"
    # ADD Sylvester the cat to the team (using append)
    # print "SYlvester the cat has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Sylvester the Cat has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Wizard of Oz World():
    # We will state the location of the user
    # If there is none return False
    # IF_GRANNY_IS_AVAILABLE_THEN
    # print " Granny is here!"
    # ADD Granny to team (using append)
    # print " Granny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Granny has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Hogwarts():
    # We will state the location of the user
    # If there is none return False
    # IF DAFFY_DUCK_IS_AVAILABLE THEN
    # print "Daffy Duck is here!"
    # ADD Daffy Duck to team (using append)
    # print "Daffy duck has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Daffy Duck has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE

# DEF Casablanca World():
    # We will state the location of the user 
    # If there is none return False
    # IF_TWEETY_IS_AVAIBLE_THEN
    # print "Tweety is here!" 
    # ADD Tweety to the team (using append)
    # print " Tweety has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Tweety has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE

# DEF Thundera():
    # We will state the location of the user
    # If there is none return False
    # IF_PORKY_THE_PIG_IS_AVAILABLE_THEN
    # print "Porky Pig is here!"
    # ADD Porky pig to team (using append)
    # Print "Porky Pig has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "Porky Pig has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE

# DEF Serververse():
    # We will state the location of the user
    # If there is none return False
    # IF AL_G_RYTHM_IS_HERE_THEN
    # print " Al-g-rythm- is here!"
    # DESTROY Al g rythm
# IF at least 7 players are recruites then they have the option to go to the final world which will be the next function
# Entering Toon World (final boss)
# IF player has at least 7 recruits AND required items:
# Start the final boss encounter.
# Final boss uses more complex attack patterns and higher health.
# Combat follows same mechanics, but with stronger enemy moves, team abilities, and special win conditions (e.g., Looney Meter).
# IF player defeats final boss:
# Game declares victory.
# Offer to play again.
# IF player loses:
# Trigger restart logic.
# Restart / replay logic
# Restarting the game (either after loss or when player chooses to replay)
# Reset all the main variables to their starting values:
# player_team ← empty list
# visited_worlds ← empty list
# items_collected ← empty list
 # enemy_status ← mark all enemies alive
# DEF Toon World():
    # We will state the location of the user
    # From each world they must recruit a player to move on to the next world
    # Make if statements to direct you to the rooms 
    # We will start with a function using nested loops or what if statements

# After certain events (recruiting a character, finding an item, winning a fight), the game updates player_stats.
# Example: recruit LeBron → increase Shooting by 2.
# Example: drink ACME Power Drink → increase Strength for two fights.
# Whenever a stat changes, recalculate any derived values (like player_health if Stamina changed).
    
    
    # Define the function for the score taker for the final game.
    # Their scores will be Measured by using the Looney Meter







