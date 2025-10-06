# MR 2nd Rock paper scissors
import random
import time

print("Welcome to Rock Paper Scissors")

options = ["Rock", "Paper", "Scissors"]

while True:
    print("What would you like to do? ")
    choice = input("Enter your choice(1-4): ")

    if choice is "1":
        print("You chose Rock!")

        if choice is "2":
            print("You chose Paper!")

            if choice is "3":
                print("You chose Scissors!")

                if choice is "4":
                    print("Thank you for playing!")

