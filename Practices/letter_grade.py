# MR 2nd What is My grade

grade = float(input("What is your grade percentage: "))

if grade >=90:
    print(f"Your grade percnetage is {grade}%, You have an A.")
elif not grade:
    print("Please enter your grade percentage.")
else:
    print("Please enter a real grade percentage.")
if grade >=80:
    print(f"Your grade percentage is {grade}%, You have a B.")
elif not grade:
    print("Please enter your grade percentage.")
if grade >=70:
    print(f"Your grade percentage is {grade}%, You have a C.")
elif not grade:
    print("Please enter your grade percentage.")
if grade>=60:
    print(f"Your grade percentage is {grade}%, You have a D.")
elif not grade:
    print("Please enter your grade percentage.")
if grade <=59:
    print(f"Your grade percentage is {grade}%, You have and F.")
elif not grade:
    print("Please enter your grade percentage.")
else:
    print("Please enter a real grade percenage.")

