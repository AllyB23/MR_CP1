# MR 2nd User Sign in

user_name = input("What is your username:\n").strip()
passwords = input("What is your Password:\n").strip()

user= "AllyB23"
password = "Verticalslabs456"

if user_name:
    if user_name == user:
        if passwords:
            if passwords == password:
                print("Hello")
            else:
                print("Your password does not match up, Please try again")
        else:
            print("You did not enter a password, Please try again")
    
    else:
        print("Your username does not match up, Please try again")
else:
    print("You did not enter a username, Please try again")
