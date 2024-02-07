# Day 5

# For loop
"""
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")
print(fruits)
"""

# For Loop with Range
"""
for number in range(1, 11, 3): # It will exclude last digit
    print(number)
"""
"""
total = 0
for num in range(1, 101):
    total += num
print(total)
"""

# Fizz Buzz Program
# Instructions: Print "Fizz" if number is divisible by 3, print "Buzz if number is divisible by 5" and print "FizzBuzz" if number is divisible by both 3 and 5
"""
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
"""


# Day 5 Project : Password Generator
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+', '^']


print("welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in password?\n"))
symbol = int(input("How namy symbols would you like?\n"))
number = int(input("How namy numbers would you like?\n"))

password_list = []

for char in range(1, letters + 1):
    #random_char = random.choice(letters_list)
    #password_list = password_list + random_char
    password_list.append(random.choice(letters_list))
for sym in range(1, symbol + 1):
    #random_sym = random.choice(symbols_list)
    #password_list = password_list + random_sym
    password_list.append(random.choice(symbols_list))
for num in range(1, number + 1):
    #random_num = random.choice(numbers_list)
    #password_list = password_list + random_num
    password_list.append(random.choice(numbers_list))

#print(f"Your password is {password_list}")
random.shuffle(password_list)


password = ""
for chara in password_list:
    password += chara
print(f"Ypur passowrd id {password}")

