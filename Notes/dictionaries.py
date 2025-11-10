# MR 2nd Dictionaires notes
avatar = {
    "earth": {
        "Toph": "My name is Toph, cuz it sounds like TOUGH and thats hust what I am>"
    },
    "water":{
        "Katara": "Its not like I am a prachy crybaby who can't help but make speaches about hope all the time.",
        "Sokka": "I used to be boomerang guy."
    }
}


person = {
    #Key: Value,
    "name": "Katie",
    "age": 37,
    "job": "coordinator",
    "siblings": [ "Alex", "Andrew", "Vienna", "Tia", "Treyson", "xavier", "Jake" ]
}

print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
    else:
        print(f"{key} is {person[key]}")
print(person.values())
person["age"] += 1
print(person["age"])
person["birthday"] = "June 8"
