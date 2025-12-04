# MR 2nd Final Project Pseudocode
# We Will welcome the user into the game
# Print("Welcome to Serverse Showdown!")
# "Welcome to Serververse Showdown. The game has been hacked, the players are missing, and it's up to you to assemble the ultimate team and reclaim the court. Ready to play for a chance at freedom?"
# We will explain the plot of the game using print statements
# EXPLANATION
# We will give the user a variable named Character so they can choose what character to be from the three options
# The options will be LeBron James, Lola Bunny, and Daffy Duck.
# We will make other variables that establish the stats of all the players.
# No matter what character they choose they will have the same stats but they have different abilities
# VARIABLES
#Lola Bunny: {}
#Bugs Bunny: {}
#Tweety: {}
#Granny: {}
#LeBron James: {}
#Daffy Duck: {}
#Porky Pig: {}
# Sylvester_the_cat: {}
# Inside of the characters dictionaries we will put these variables:
""" Basketball_IQ:[]
    Stamina/Durability:[]
    Looney_Ablilities:[]
    Strength:[]
    Speed:[]
    Shooting:[]
    """
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
# ANOTHER VARIABLE """TEAM""""!!!!!!!!!
# The user can basically choose what world or room is there starting one because there is not a set starting point
# They will have the option to go to whatever world they like from the random 3 that they are given
# User input to ask them what world they would like to go to
# VARIABLE we will have a variable that updates when the user chooses to go to another world.
# IF statements to decide which world to travel because they only have the the option of 3 to choose from
# IF character = 1 go to Earth
# Elif character = 2 go to 
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




# DEF DC World():
    # We will state the locaiton of the user
    # If the character is Daffy Duck then the player will come to this room/world and choose who to go recruit next
    # If there is none return False
    # IF_LOLA_BUNNY_IS_AVIALBLE_THEN
    # print "Lola Bunny is here!"
    # ADD Lola bunny to team (using append)
    # print "Lola Bunny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Mad Max Universe():
    # We will state the locaiton of the user
    # if the character is Bugs Bunny the player wil start out on Mad Max Universe
    # If there is none return False
    # IF BUGS_BUNNY_IS_AVAILABLE THEN
    # print "Bugs Bunny is here!"
    # ADD Bugs Bunny to team (using append)
    # print "Bugs bunny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
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
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Wizard of Oz World():
    # We will state the locaiton of the user
    # If there is none return False
    # IF_GRANNY_IS_AVAILABLE_THEN
    # print " Granny is here!"
    # ADD Granny to team (using append)
    # print " Granny has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE



# DEF Hogwarts():
    # We will state the locaiton of the user
    # If there is none return False
    # IF DAFFY_DUCK_IS_AVAILABLE THEN
    # print "Daffy Duck is here!"
    # ADD Daffy Duck to team (using append)
    # print "Daffy duck has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE

# DEF Casablanca World():
    # We will state the locaiton of the user 
    # If there is none return False
    # IF_TWEETY_IS_AVAIBLE_THEN
    # print "Tweety is here!" 
    # ADD Tweety to the team (using append)
    # print " Tweety has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE


# DEF Serververse():
    # We will state the locaiton of the user
    # If there is none return False
    # IF AL_G_RYTHM_IS_HERE_THEN
    # print " Al-g-rythm- is here!"
    # DESTROY Al g rythm


# DEF Thundera():
    # We will state the locaiton of the user
    # If there is none return False
    # IF_PORKY_THE_PIG_IS_AVAILABLE_THEN
    # print "Porky Pig is here!"
    # ADD Porky pig to team (using append)
    # Print "Porky Pig has joined the toon squad!"
        # Return TRUE to indicate successful recruitment
       # RETURN TRUE
    #ELSE
       # PRINT "LeBron James has already been recruited or is unavailable."
        # Return FALSE if no player was found, preventing movement without purpose
        #RETURN FALSE

# IF at least 7 players are recruites then they have the option to go to the final world which will be the next function

# DEF Tune World():
    # We will state the locaiton of the user
    # From each world they must recruit a player to move on to the next world
    # Make if statements to direct you to the rooms 
    # We will start with a function using nested loops or what if statements
    # Their scores will be Measured by using the Looney Meter





