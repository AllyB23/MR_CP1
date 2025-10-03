# MR 2nd While loops notes
import time
import random

#Infinite loop
num = 0
break_point = random.randint(1,50)
while num < 20:
    num += 1 #fixed the loop
    if num == break_point:
        break
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(.10)
else:
    print("This loop exited by meeting the condition!")
 
print("The loop is over")