#  MR 2nd random numbers notes
import random

print(random.random()) # Float between 0 and 1

print(random.randint(1, 6))


name = input("What is your name: \n").strip().title()

# Random stat creator D&D
stat_one = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_two = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_three = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_four = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_five = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_six = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)
stat_seven = random.randint(1,6)+ random.randint(1,6) + random.randint(1,6)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}. {stat_seven}")

# Set individual stats