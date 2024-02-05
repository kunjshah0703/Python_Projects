# Day 3 - Of Python Coding

#Program to check if person can ride rollercoaster or not ?
"""
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7:")
    elif age >= 45 and age <= 55:
        print(f"Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    #else:
        #print(f"Your final bill is ${bill}")
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")

"""
# Program for BMI calculator based on various bmi ranges
    
"""
height = float(input("Enter your height in meters? Example 1.55 ?  "))
weight = int(input("Enter your weight in kilograms ? "))

bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
"""

# Program to check if the given year is leap yera or not:
"""
year = int(input("Enter year? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

"""

#Program to calculate final bill of pizza

"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ") #

final_bill = 0

if size == 'S':
  final_bill += 15
elif size == "M":
  final_bill += 20
else:
  final_bill += 25

if add_pepperoni == 'Y':
    if size == "S":
       final_bill += 2
    else: 
       final_bill += 3

if extra_cheese == "Y":
   final_bill += 1

print(f"Your final bill is: ${final_bill}.")

"""


# Love Calculator
"""
print("The Love Calculator is calculating your score...")
name1 = input("Enter name? ")
name2 = input("Enter name? ")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second = l + o + v + e

score = int(str(first) + str(second))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

"""


# Day 3 Project - Treasure Island


print("welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go? Type ""left"" or ""right"" ?")

if choice == "left":
    print("You came to a lake. There is an island in the middle of the lake")
    swi_wait = input("Type ""wait"" to wait for a boat. Type ""swim"" to swim across.")
    swim_wait = swi_wait.lower()
    if swim_wait == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        color_choose = input("Which color do you choose? ")
        colour_choose = color_choose.lower()
        if colour_choose == "yellow":
            print("You Win!")
        elif colour_choose == "red":
            print("It's a room full of fire. Game over.")
        elif colour_choose == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")