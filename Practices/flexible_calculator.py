# MR 2nd Flexible calculator

# write a print statement that welcome sthe user into the flexible calculator
print("Welcome to the Flexible Calculator!")
# We will make args to show the avaiable operations we cand o for the calculator
print("What operation would you like to perform?")
options = int(input(
    "1.Average\n"
    "2.Maximum\n"
    "3.Minimum\n"
    "4.Sum\n"
    "5.Product\n"))

how_many_numbers = int(input("How many numbers will you be using? "))
numbers = []

for i in range(how_many_numbers):
     numbers_list= int(input("Number: "))
     numbers.append(numbers_list)



def average(*nums):
    nums = nums[0]
    if not nums:
          return None
    total_sum = sum(nums)
    count = len(nums)
    return total_sum / count


def maximum(*nums):
        nums = nums[0]
        return max(*nums)


def sum(*nums):
    nums = nums[0]
    total = 0
    for num in nums:
        total += sum
    return total


def minimum(*nums):
        nums = nums[0]
        return min(*nums)


def product(*nums):
      nums = nums[0]
      product = 0
      for product in nums:
            product *= nums
            return product
      

result = None
operations_name = ""


if options == 1:
    result = average(numbers)
    operation_name = "Average"
    print(result)
elif options == 2:
    result = maximum(numbers)
    operation_name = "Maximum"
    print(result)
elif options == 3:
    result = minimum(numbers)
    operation_name = "Minimum"
    print(result)
elif options == 4:
    result = sum(numbers)
    operation_name = "Sum"
    print(result)
elif options == 5:
    result = product(numbers)
    operation_name = "Product"
    print(result)

else:
     print("That is not valid.")

                     



# you want atnoeher function ot check if the number they input is an integer or a float
# you want to do an isinstance for calculating the numbers that they inputtedted and also the fucntions that they inputted
# after all that you want to ive them the option to keeo going and do smome more calculations or the option ot be done por exit.
