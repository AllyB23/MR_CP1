# MR 2nd Mapping notes

numbers = [321,6,546,547,4764,754,6,4365,435,5]
""""divided = []"""

"""for num in numbers:
    divided.append(num/2)"""

def divide(number):
    return number/2

divided = map(lambda num: num/2, numbers)

#for i, num in enumerate(numbers):
    #print(f"{num} divided by 2 is {divided[i]}")