# 1. Decisions at the Crossroad

# Task 1: Code Correction
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#2 The Greatest Showdown

# Task 1: Identify the Greatest
num1 = 3 
num2 = 65
num3 = 21
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)

# Task 2: Identify the Smallest
if (num1 <= num2) and (num1 <= num3):
   smallest = num1
elif (num2 <= num1) and (num2 <= num3):
   smallest = num2
else:
   smallest = num3
print("The smallest number is", smallest)

# Task 3: Equality Check

num1 = 7
num2 = 7
num3 = 7

if num1 == num2 == num3:
    print("They're all equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two of the number are equal")

# 3. Leap Year Explorer

year = int(input("Please enter a year: "))
if year % 4 == 0:
   if year % 400:
      print("This is a leap year!")
   elif year % 100:
      print("This is not a leap year!")
   else:
      print("Also a leap year!")
else:
   print("Also not a leap year!")
