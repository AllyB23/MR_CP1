#MR 2nd passwrod strength project
# In all of these if statements we tell the user we add 1 point or subtract one point from their strentgh score

import string

# We set up an input for the user to input their password and establish a variable for the total score of their password strength
password = input("Please enter a password: ")
strength_score = 0

# we first check password length using an if statement
if len(password) >= 8:
    print("Your password is long enough, +1")
    strength_score += 1
else:
    print("Your password is not long enough, -1")

# we then check for uppercase letters using an if statement
upper_found = False
for char in password:
    if char.isupper():
        upper_found = True
        break
if upper_found:
    print("Yes, Contains uppercase")
    strength_score += 1
else:
    print("Your password does not have an uppercase letter")

# we check for lowercase letters using an if statemnt and making sure that there is a lowercase letter in the password
lower_found = False
for char in password:
    if char.islower():
        lower_found = True
        break
if lower_found:
    print("Yes, contains lowercase")
    strength_score += 1
else:
    print("Your password does not have a lowercase letter")

# we then check if there is a number in the password 
digit_found = False
for char in password:
    if char.isdigit():
        digit_found = True
        break
if digit_found:
    print("Yes, contains a number")
    strength_score += 1
else:
    print("Your password does not contain a number")

# At last we check if the password has any special characters
special_found = False
special_chars = string.punctuation
for char in password:
    if char in special_chars:
        special_found = True
        break
if special_found:
    print("Yes, contains special character")
    strength_score += 1
else:
    print("Your password does not have a special character")

# After the password is checked we tell the user their strength score out of 5 using a print statement
print(f"Your password has a {strength_score}/5 strength score.")