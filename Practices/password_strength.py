# MR 2nd password strength checker
import string

# We set up an input for the user to input their password and establish a variable for the total score of their password strength
password = input("Please enter a password: ")
strength_score = 0
length = 0
upper = 0
lower = 0
digit = 0
special = 0
# After they have entered a password we have to check if the password is long enough
def check_password_length(password):

    if len(password) >=8:
        return True
    else:
        return False
        if True:
            print("Your password is long enough, +1")
            strength_score += 1
        if False:
            print("Your password is not long enough, -1")
# if it is long enough we have to check if there is an uppercase letter in the password
def has_uppercase_loop(password):
    global upper
    for char in password:
        if char.isupper():
            upper = True
    upper = False
if upper == False:
    print("Your password does not have an uppercase letter")
if upper == True:
    print("Yes, Contains uppercase")
    strength_score += 1
# After that we check if the password contans a lowercase letters
def has_lowercase(password):
    global lower
    lower = any(char.islower() for char in password)
if lower == False:
    print("Your password does not have a lowercase letter")
if lower == True:
    print("Yes, contains lowercase")
    strength_score += 1

# After that we check if the password contains atleast one number 
def has_digit_loop(password):
    global digit
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
            break
        return digit
if digit == False:
    print("Your password does not contain a number")
if digit == True:
    print("Yes, contains a number")
    strength_score += 1

# after that we check if the password contains at least one special character
def has_special_character(password):
    global special
    special_chars = string.punctuation
    for char in password:
        special = True
    special = False
if special == True:
    print("Yes, contains special character")
    strength_score =+ 1
if special == False:
    print("Your password does not have a special character")

#  After the password is checked and all of those things are true we respond to the user and tell them that there password is strong
print(f"Your password has a {strength_score}/5 strength score.")
# If there password does not check some of those if and elifs then we must tell them their strength score
