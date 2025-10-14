# MR 2nd Fix game assignment
# One of the bugs was that the number that the user inputed has to be a float.
# Another one of the bugs was on line 18 they needed an Elif instead of an if.
# were not increasing the number of our attempts anywhere this is a logic error

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1,100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input(float("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. the number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        continue
    print("Game over. Thanks for playing!")
start_game