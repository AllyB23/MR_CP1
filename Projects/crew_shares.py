# MR 2nd Crew Shares Project

money = float(input("What is the total amount of money?").strip())
print("There is this much money: ", money)
crew_members = int(input("How many crew members are there? " ).strip())
shares = money/(crew_members+10)
captain_share = shares*7
first_mate = shares*3
crew_share = shares-500
print(f"The captain's share is ${captain_share:.2f} \n The first mate's share is ${first_mate:.2f} \n The rest of the crew's shares is ${crew_share:.2f} \n for each member")