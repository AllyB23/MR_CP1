# MR 2nd Rock paper scissors
import random
import time

print("Welcome to Rock Paper Scissors")

options = ["rock", "paper", "scissors"]

while True:
    user = input( "rock, paper, scissors, or exit: ")

    if user == "exit":
        print("Thank you for playing!")
        break
    if user not in options:
        print("That's not one of the choices. ")
        continue

    com = random.choice(options)
    print(f"I chose {com}. ")

    if user == com:
        print("It's a tie!\n")
    elif (user == "rock" and com =="scissors") or \
         (user == "scissors" and com =="paper") or \
         (user == "paper" and com =="rock"):
         print("You win!\n")
    else:
        print("You lose...")


