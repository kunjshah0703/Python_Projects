# Day 4

# Working with random module
"""
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)
"""

# Head and Tails Program
"""
import random

head_tail = random.randint(0,1)
if head_tail == 1:
    print("Heads")
else:
    print("Tails")
"""

# List in Python
"""
states_of_india = ["Maharashtra", "Karnataka", "Gujarat", "Madhya Pradesh"]

states_of_india[0] ="MH"
#print(states_of_india)

states_of_india.append("Telengana")
states_of_india.extend(["Andra Pradesh", "Arunachal Pradesh"])
print(states_of_india)
"""


# Program to know who is going to pay bill today
"""
names_string = ["Kunj", "Rohan", "Gorang"]
names = names_string.split(", ")

import random

num_items_names = len(names)

random_choice = random.randint(0, num_items_names - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
"""

# Day 5 : Project Rock Paper and Sissor
import random
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
   print("You won!")
elif (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
   print("It's a draw!")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice== 0) or (computer_choice == 2 and user_choice == 1):
   print("Computer Won!")