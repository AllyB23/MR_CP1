# MR 2nd Conditionals notes
import random
monster_hp = 30
dmg_modifier = 2
atck_bonus = 3
player_hp = 25

roll = random.randint(1,20)

if roll == 20:
    print("You succeed! {}")
    attack = random.randint(1,8) + random.randint(91,8) + dmg_modifier
    monster_hp -= attack 
    print(f"You did {attack} damamge to the monster!")
elif roll+atck_bonus > 10:
    print(f"Ypu hit!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"you did {attack} damage to the monster!")
elif roll <=10:
    if roll == 1:
        print(f"You rolled a cirtical failure! The monster gets a free attack!")
        damage = (random.randint(1,10) +2)
        player_hp -= damage
        print(f(f"You took {damage} you now have {player_hp} HP,"))
    else:
        print("You missed!")
else:
    print("That shouldn't be possible!")

print("Your turn is over.")

if monster_hp and monster_hp > 0:
    print("It is the monsters turn")
else:
    print("the monster is dead")