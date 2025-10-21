# MR 2nd functions notes
# All imports
# set global varirables
num = 0
player_hp = 100
monster_hp = 100

# write your functions
def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg):
    if turn == "Player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg


#Write the rest of the code
while num < add(5,5):
    print("Duck")
    num+=1
print("Goose")
print(f"Results is: {add(-123,123456)}")
total = add(9658765,78904567)




monster_hp, player_hp = attack(15, "player")
print(f"Tia's intials are: {initials("Tia laRose")}")
print(f"Xavier's intnitals are : {initials("Xavier laRose")}")

monster_hp, player_hp = attack(15, "player")
print(f"PLayer health: {player_hp}")
print(f"Monster health: {monster_hp}")
