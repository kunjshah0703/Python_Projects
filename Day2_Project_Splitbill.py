# If I want to print number of digits

#print(len(1234)) # Gives error because there is no int function for len

#print("Hello"[4])

#print("123" + "345") # Treated as string

# Integer

#print(123 + 345)

# Float

#print(type(3.14159))

# Boolean -- Only two possible values True and False

# Program for converting from int to str
"""
num_char = len(input("What is your name? "))
#print(f"Your name has {num_char} characters.")
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")"""

"""Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8"""

"""
two_digit_number = input()
num1 = two_digit_number[0]
num2 = two_digit_number[1]
print(int(num1) + int(num2))"""

# Checking the precendence of operators print(3 * (3 + 3) / 3 - 3)

"""Write a program to calcualte BMI of person.
NOTE: You should convert the bmi to a whole number and print out a whole number
BMI is calculated by weight/(height)*(height)"""

"""
height = input("Enter height in meters: ")

weight = input("Enter weight in kilograms: ")

new_height = float(height)
new_weight = float(weight)

bmi = new_weight / (new_height * new_height)
#print(type(bmi))
print(int(bmi))"""

"""Write a program to calculate number of weeks reamining.
Considering you live uptil 90 years."""

"""
age = input("Enter your age : ")
max_age = 90
weeks_left = (max_age - int(age)) * 52
print(f"You have {weeks_left} weeks left.")"""


# Day 2 Final Project

# Project : Tip Calculator

print("Welcome to the tip calculator.")
total_bill = int(input("What was total bill? "))
percentage_of_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

intial_bill_after_split = (total_bill / total_people)
adding_tip_percent = intial_bill_after_split * (percentage_of_tip/100)
final_bill = round(intial_bill_after_split + adding_tip_percent,2)
print(f"Each person should pay rupees {final_bill} : ")