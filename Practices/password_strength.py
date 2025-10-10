# MR 2nd password strength checker
import string

# We set up and input for the user to input their password and establish a variable for the total score of their password strength
password = input("Please enter a password: ")
strength_score = 0
# After they have entered a password we have to check if the passwor di s long enough
if password:
    print("Thank you for entering your password!")
else:
    print("No password entered.")

# if it is long enough we have to check if there is an uppercase letter in the password
def has_uppercase_loop(password):
    for char in password:
        if char.isupper():
            return True
    return False
if False:
    print("-1")
if True:
    print("+1")
# After that we check if the password contans a lowercase letters
def has_lowercase(password):
    return any(char.islower() for char in password)

# After that we check if the password contains atleast one number 
def has_digit_loop(password):
    for char in password:
        if char.isdigit():
            return True
        return False
if False:
    print("-1")
if True:
    print("+1")

# after that we check if the password contains at least one special character
def has_special_character(password):
    special_chars = string.punctuation
    for char in password:
        return True
    return False
if True:
    print("+1")
if False:
    print("-1")

#  After the password is checked and all of those things are true we respond to the user and tell them that there password is strong
# If there password does not check some of those if and elifs then we msut tell them their strength score
