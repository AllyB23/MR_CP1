# MR 2nd What is My grade

grade = float(input("What is your grade percentage: "))

if grade >=90:
  print(f"Your grade percentage is {grade}% and you have an A.")
elif grade >= 80:
  print(f"Your grade percentage is {grade}% and you have a B.")
elif grade >=70:
  print(f"Your grade percentage is {grade}% and you have a C.")
elif grade >=60:
  print(f"Your grade percentage is {grade}% and you have a D.")
else:
  print(f"Your grade percentage is {grade}% and you have an F.")
