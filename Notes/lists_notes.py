# MR 2nd Lists Notes
import random

names = ["Alex", "katie", "Cora, 'Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[3])
print(names[random.randint(1, len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names.remove(3.14)
x = names.index(5)
names.insert(3, "Vienna")
names.pop(x)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][1] = "X"

print(board)
# Lists (changeable, ordered)
# Tuple (Not changeable, ordered)
classes = ("Bard", "Monk", "Barabrians", "paladin")

# Set (changeable, unordered)
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)