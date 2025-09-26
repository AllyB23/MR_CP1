# MR 2nd What is My grade

grade = float(input("What is your grade percentage: "))

if grade >=90:
    print(f"Your grade percentage is {grade}%, You have an A.")
if grade >=80:
    print(f"Your grade percentage is {grade}%, You have a B.")
if grade >=70:
    print(f"Your grade percentage is {grade}%, You have a C.")
if grade >=60:
    print(f"Your grade percentage is {grade}%, You have a D.")
if grade <=59:
    print(f"Your grade percentage is {grade}%, You have and F.")
else:
    print("Please enter a real grade percenage.")
