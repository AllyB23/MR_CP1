# MR 2nd What is My grade

grade = float(input("What is your grade percentage: "))

if grade >=90:
    print(f"Your grade percentage is {grade}%, You have an A.")
elif grade >=80:
    print(f"Your grade percentage is {grade}%, You have a B.")
elif grade >=70:
    print(f"Your grade percentage is {grade}%, You have a C.")
elif grade >=60:
    print(f"Your grade percentage is {grade}%, You have a D.")
elif grade <=59:
    print(f"Your grade percentage is {grade}%, You have and F.")
else:
    print("Please enter a real grade percenage.")
