#This file has many Python exercises to practice with. Everything to learn in introductory and object oriented Python is in this file. 
#To run or test the code blocks, remove the comments with CTRL + /. 

# #Lesson 1 Variables
# # Variable = A container for a value (string, integer, float, boolean)
# # A variable behaves as if it was the value it contains

# # Strings
# first_name = "Bob"
# food = "pizza"
# email = "bob@email.com"

# # Integers
# age = 25
# quantity = 3
# num_of_students = 30

# # Float
# price = 10.99
# gpa = 3.2
# distance = 5.5

# # Boolean
# is_student = True
# for_sale = False
# is_online = True

# print(f"Hello {first_name}")
# print(f"You are {age} years old")
# print(f"Your gpa is: {gpa}")

# if is_student:
#     print("You are a student")
# else:
#     print("You are NOT student")



# # Lesson 2. Type Casting
# # type casting = The process of converting a value of one data type to another
# #                          (string, integer, float, boolean)
# #                          Explicit vs Implicit

# name = "Bob"
# age = 21
# gpa = 1.9
# student = True

# # print(type(name))
# # print(type(age))
# # print(type(gpa))
# # print(type(student)) 

# age = float(age)
# print(age)

# gpa = int(gpa)
# print(gpa)

# student = str(student)
# print(student)

# name = bool(name)
# print(name)

# # Lesson 3. User Input
# # ------------------------------------------------
# # EXERCISE 1 MAD LIBS
# # ------------------------------------------------
# adjective1 = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# adjective2 = input("Enter an adjective: ")
# verb = input("Enter a verb: ")
# adjective3 = input("Enter an adjective: ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw {noun}.")
# print(f"{noun} was {adjective2} and {verb}ing.")
# print(f"I was {adjective3}!")

# # ------------------------------------------------
# # EXERCISE 2 AREA CALC
# # ------------------------------------------------
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# #area = length * width
# #print(f"The area is: {area}cm^2")

# # ------------------------------------------------
# # EXERCISE 3 SHOPPING CART
# # ------------------------------------------------
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))

# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: ${round(total, 2)}")

# Lesson 4. Math
# a = 10
# b = 3

# print(a + b)   # Addition → 13
# print(a - b)   # Subtraction → 7
# print(a * b)   # Multiplication → 30
# print(a / b)   # Division → 3.333...
# print(a // b)  # Floor division → 3
# print(a % b)   # Modulus (remainder) → 1
# print(a ** b)  # Exponentiation → 1000

# x = -5
# y = 3.7
# numbers = [4, 7, 1, 9]

# print(abs(x))        # Absolute value → 5
# print(round(y))      # Round → 4
# print(max(numbers))  # Maximum → 9
# print(min(numbers))  # Minimum → 1
# print(sum(numbers))  # Sum → 21

# import math

# print(math.pi)        # Value of pi
# print(math.sqrt(16))  # Square root → 4.0
# print(math.ceil(4.2)) # Round up → 5
# print(math.floor(4.9))# Round down → 4
# print(math.pow(2, 3)) # Power → 8.0

# import math

# radius = float(input("Enter radius: "))
# circumference = 2 * math.pi * radius

# print("Circumference:", circumference)

# import math

# radius = float(input("Enter radius: "))
# area = math.pi * radius ** 2

# print("Area:", area)

# import math

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))

# hypotenuse = math.sqrt(a ** 2 + b ** 2)


# print("Hypotenuse:", hypotenuse)



# # Lesson 5. if, else if, else
# # if = Do some code IF condition is True
# # else = Do something else if above condition/s are False

# # —---------------------
# #   EXAMPLE 1
# # —---------------------
# age = int(input("Enter your age: "))

# if age >= 100:
#    print("You are too old to sign up")
# elif age >= 18:
#    print("You are now signed up")
# elif age < 0:
#    print("You haven't been born yet")
# else:
#    print("You must be 18+ sign up")

# # —---------------------
# #   EXAMPLE 2
# # —---------------------
# response = input("Do you want food (Y/N)?: ")

# if response == "Y":
#    print("Have some food")
# else:
#    print("No food for you!")

# # —---------------------
# #   EXAMPLE 3
# # —---------------------
# name = input("Enter your name: ")

# if name == "":
#    print("You did not enter your name!")
# else:
#    print(f"Hello {name}")

# # —---------------------
# #   EXAMPLE 4
# # —---------------------
# online = False

# if online :
#    print("You are online")
# else:
#    print("You are offline")


# Lesson 6. Simple Calculator
# operator = input("Enter an operator (+ - * / ** % //): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# elif operator == "**":
#     result = num1 ** num2
#     print(round(result, 3))
# elif operator == "%":
#     result = num1 % num2
#     print(round(result, 3))
# elif operator == "//":
#     result = num1 // num2
#     print(int(result))
# else:
#     print(f"{operator} is not a valid operator")


# Lesson 7. Weight Converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not valid")


# # Lesson 8. Temperature Conversion
# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}°F")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"The temperature in Celsius is: {temp}°C")
# else:
#     print(f"{unit} is an invalid unit of measurement")



# # Lesson 9. Logical Operators
# # logical operators = used on conditional statements

# #              and = checks two or more conditions are True
# #               or = checks if at least one condition is True
# #              not = True if condition is False, and vice versa

# temp = 20
# sunny = True

# if temp <= 0 or temp >= 30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")

# if not sunny:
#     print("It is cloudy")
# else:
#     print("It is sunny")


# Lesson 10. Conditional Expressions
# # conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# #                                             Print or assign one of two values based on a condition
# #                                             X if condition else Y

# num = 5
# a = 6
# b = 7
# age = 13
# temperature = 20
# user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"


# # Lesson 11. String Methods
# # -------------------------------
# # STRING METHODS
# # -------------------------------
# # name = input("Enter your name: ")
# # phone_number = input("Enter your phone #: ")

# # length = len(name)
# # index = name.find(" ")
# # name = name.capitalize()
# # name = name.upper()
# # name = name.lower()
# # result = name.isdigit()
# # result = name.isalpha()
# # result = phone_number.count(" ")
# # phone_number = phone_number.replace("-", "")

# # -------------------------------
# #        EXERCISE
# # -------------------------------
# username = input("Enter a username: ")

# if len(username) > 12:
#    print("Your name can't be more than 12 characters")
# elif not username.find(" ") == -1:
#    print("Your username can't contain spaces")
# elif not username.isalpha():
#    print("Your username can't contain digits")
# else:
#    print(f"Welcome {username}!")


# # Lesson 12. String Indexing
# # indexing = accessing elements of a sequence using [] (indexing operator)
# #                     [start : end : step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[:4])
# print(credit_number[4:8])
# print(credit_number[4:])
# print(credit_number[-1])
# print(credit_number[-4:])
# print(credit_number[::2])
# print(credit_number[::3])

# # EXERCISE 1
# credit_number = "1234-5678-9012-3456"
# # last_digits = credit_number[-4:]
# # print(f"XXXX-XXXX-XXXX-{last_digits}")

# # EXERCISE 2
# credit_number = "1234-5678-9012-3456"
# credit_number = credit_number[::-1]
# print(credit_number)


# # Lesson 13. Email Slicer Program
# email = input("Enter your email: ")

# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]

# print(f"Your username is {username} and domain is {domain}")



# # Lesson 14. Format Specifiers
# # format specifiers = {:flags} format a value based on what flags are inserted

# # .(number)f = round to that many decimal places
# # :(number) = allocate that many spaces
# # :0(number) = allocate and zero pad that many spaces
# # :< = left justify
# # :> = right justify
# # :^ = center align
# # :+ = use a plus sign to indicate positive value
# # := = place sign to leftmost position
# # :  = insert a space before positive numbers
# # :, = comma separator
# # :% = percentage format

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price1 is: ${price1:}")
# print(f"price2 is: ${price2:}")
# print(f"price3 is: ${price3:}")


# # Lesson 15. While Loops
# #while loop = perform some code WHILE some condition remains true

# # ---------------- EXAMPLE 1 ----------------

# name = input("Enter your name: ")

# while name == "":
#    print("You did not enter your name!")
#    name = input("Enter your name: ")

# print(f"Hello {name}")

# # ---------------- EXAMPLE 2 ----------------

# age = int(input("Enter your age: "))

# while age < 0:
#    print("Age can't be negative")
#    age = int(input("Enter your age: "))

# print(f"You are {age} years old")


# # ---------------- EXAMPLE 3 ----------------

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another food you like (q to quit): ")

# print("bye")

# # ---------------- EXAMPLE 4 ----------------

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"You picked the number {num}")


# # Lesson 16. Interest Calculator
# # Python compound interest calculator

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than zero")
#     else:
#         break

# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than zero")
#     else:
#         break

# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero")
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")


# # Lesson 17. For Loops
# # for loops = execute a block of code a fixed number of times.
# #                     You can iterate over a range, string, sequence, etc.

# # ---------------- EXAMPLE 1 ----------------

# for x in range(1, 11):
#    print(x)

# # ---------------- EXAMPLE 2 ----------------

# for x in reversed(range(1, 11)):
#    print(x)

# print("Happy New Year!")

# # ---------------- EXAMPLE 3 ----------------

# for x in range(1, 11, 2):
#    print(x)

# # ---------------- EXAMPLE 4 ----------------

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#    print(x)

# # ---------------- CONTINUE ----------------

# for x in range(1, 21):
#    if x == 13:
#        continue
#    else:
#        print(x)

# # ---------------- BREAK ----------------

# for x in range(1, 21):
#    if x == 13:
#        break
#    else:
#        print(x)


# # Lesson 18. Nested Loops
# # nested loop = A loop within another loop (outer, inner)
# #                          outer loop:
# #                              inner loop:

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#    for y in range(columns):
#        print(symbol, end="")
#    print()


# # Lesson 19. Countdown Timer
# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")


# Lesson 20. Lists, Sets, Tuples
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# # Lesson 21. Shopping Cart Program
# # Shopping cart exercise

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print()
# print(f"Your total is: ${total}")



# # Lesson 22. 2D Collections
# # 2D list of lists
# num_pad = [[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"]]

# # 2D list of tuples
# num_pad = [(1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#")]

# # 2D list of sets
# num_pad = [{1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"}]

# # 2D tuple of lists
# num_pad = ([1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"])

# # 2D tuple of tuples
# num_pad = ((1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#"))

# # 2D tuple of sets
# num_pad = ({1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"})

# # 2D set of lists (NOT VALID)
# num_pad = {[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"]}

# # 2D set of tuples
# num_pad = {(1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#")}

# # 2D set of sets (NOT VALID)
# num_pad = {{1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"}}

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


# # Lesson 23. Quiz Game
# questions = ("How many elements are in the periodic table?: ",
#                        "Which animal lays the largest eggs?: ",
#                        "What is the most abundant gas in Earth's atmosphere?: ",
#                        "How many bones are in the human body?: ",
#                        "Which planet in the solar system is the hottest?: ")

# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#                    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#                    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#                    ("A. 206", "B. 207", "C. 208", "D. 209"),
#                    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1

# print("----------------------")
# print("       RESULTS        ")
# print("----------------------")

# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")


# Lesson 24. Dictionaries
# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C.",
#                     "India": "New Delhi",
#                     "China": "Beijing",
#                     "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# values = capitals.values()
# for value in capitals.values():
# print(value)

# items = capitals.items()
# for key, value in capitals.items():
#    print(f"{key}: {value}")


# # Lesson 25. Concession Stand Program
# # Concession stand program

# menu = {"pizza": 3.00,
#                "nachos": 4.50,
#                "popcorn": 6.00,
#                "fries": 2.50,
#                "chips": 1.00,
#                "pretzel": 3.50,
#                "soda": 3.00,
#                "lemonade": 4.25}
# cart = []
# total = 0

# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("------ YOUR ORDER ------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: ${total:.2f}")


# # Lesson 26. Random Class
# import random

# low = 1
# high = 100
# options = ("Rock", "Paper", "Scissors")
# cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# # number = random.random()
# # number = random.randint(low, high)
# # choice = random.choice(options)
# # random.shuffle(cards)

# # -------------- NUMBER GUESSING GAME --------------

# import random

# low = 1
# high = 100
# guesses = 0
# number = random.randint(low, high)

# while True:
#    guess = int(input(f"Enter a number between ({low} - {high}): "))
#    guesses += 1

#    if guess < number:
#        print(f"{guess} is too low")
#    elif guess > number:
#        print(f"{guess} is too high")
#    else:
#        print(f"{guess} is correct!")
#        break

# print(f"This round took you {guesses} guesses")



# # Lesson 27. Number Guessing Game
# # Python number guessing game
# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:

#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")


## Lesson 28. Rock, Paper, Scissors Game
# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")




# # Lesson 29. Dice Roller
# import random

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # PRINT VERTICALLY
# # for die in range(num_of_dice):
# #    for line in dice_art.get(dice[die]):
# #        print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")




# # Lesson 30. Encryption Program
# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# #ENCRYPT
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message : {plain_text}")
# print(f"encrypted message: {cipher_text}")

# #DECRYPT
# cipher_text = input("Enter a message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"encrypted message: {cipher_text}")
# print(f"original message : {plain_text}")


# # Lesson 31. Functions
# # ----------  EXAMPLE 1  ---------- 
# def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# # display_invoice("BobCode", 42.50, "01/01")
# # display_invoice("JoeSchmo", 100.01, "01/02")

# # ----------  EXAMPLE 2  ---------- 
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("spongebob", "squarepants")
# print(full_name)


# # Lesson 32. Default Arguments
# # ----- EXAMPLE -----
# def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1 - discount) * (1 - tax)

# # print(net_price(500))
# # print(net_price(500, 0.1))
# # print(net_price(500, 0.1, 0))

# # ----- EXERCISE -----
# import time

# def count(end, start=0): 
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")

# # count(10)
# # count(30, 15)


# # Lesson 33. # keyword arguments = arguments prefixed with the names of parameters
# #                                        order of the arguments doesn’t matter
# #                                        helps with readability

# # ----- EXAMPLE 1 -----
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", title="Mr.", last="John", first="James")

# # ----- EXAMPLE 2 -----
# for number in range(1, 11):
#     print(number, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

# # ----- EXERCISE -----
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)
# print(phone_num)


# # Lesson 34. *ARGS and **KWARGS
# # ----- *ARGS Example 1 -----

# def add(*nums):
#    total = 0
#    for num in nums:
#        total += num
#    return total

# print(add(1, 2, 3, 4))

# # ----- *ARGS Example 2 -----

# def display_name(*args):
#    print(f"Hello", end=" ")
#    for arg in args:
#        print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# # ----- **KWARGS -----
# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value, end=" ")

# print_address(street="123 Fake St.",
#               pobox="P.O Box 777",
#               city="Detroit",
#               state="MI",
#               zip="54321")

# # ----- EXERCISE -----
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('pobox')}")
#     else:
#         print(f"{kwargs.get('street')}")

#     print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Squarepants",
#                street="123 Fake St.",
#                pobox="PO box #1001",
#                city="Detroit",
#                state="MI",
#                zip="54321")


# # Lesson 35. Iterables
# # Iterables = An object/collection that can return its elements one at a time,
# #                    allowing it to be iterated over in a loop

# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_set = {"apple", "orange", "banana", "coconut"}
# my_name = "Bob"
# my_dictionary = {'A': 1, 'B': 2, 'C': 3}

# for item in my_list:
#     print(item)

# # DICTIONARIES
# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

# for key, value in my_dictionary.items():
#     print(f"{key} = {value}")


# # Lesson 36. Membership Operators
# # Membership operators = used to test whether a value or variable is found in a sequence
# #                                             (string, list, tuple, set, or dictionary)
# #                                             1. in
# #                                             2. not in

# # --------------------
# # EXAMPLE 1
# # --------------------
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#    print(f"There is a {letter}")
# else:
#    print(f"{letter} was not found")

# # --------------------
# # EXAMPLE 2
# # --------------------
# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")

# if student in students:
#    print(f"{student} is in this class")
# else:
#    print(f"{student} is NOT in this class")

# # --------------------
# # EXAMPLE 3
# # --------------------
# grades = {
#    "Sandy": 'A',
#    "Squidward": 'B',
#    "Spongebob": 'C',
#    "Patrick": 'D'
# }

# student = input("Enter the name of a student: ")

# if student in grades:
#    print(f"{student}'s grade is {grades[student]}.")
# else:
#    print(f"{student} is not in the dictionary")

# # --------------------
# # EXAMPLE 4
# # --------------------
# email = "bob@email.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# # Lesson 37. List Comprehensions
# # List comprehension = A concise way to create lists in Python
# #                                        Compact and easier to read than traditional loops
# #                                        [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# fruits = ["apple", "orange", "banana", "coconut"]
# uppercase_words = [fruit.upper() for fruit in fruits]
# fruit_chars = [fruit[0] for fruit in fruits]

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_numbers = [x for x in numbers if x >= 0]
# negative_numbers = [x for x in numbers if x < 0]
# even_numbers = [x for x in numbers if x % 2 == 0]
# odd_numbers = [x for x in numbers if x % 2 == 1]

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]


# # Lesson 38. Match-Case Statements
# # Match-case statement (switch): An alternative to using many 'elif' statements
# #                                                          Execute some code if a value matches a 'case'
# #                                                          Benefits: cleaner and syntax is more readable

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False

# print(is_weekend("Monday"))



# # Lesson 39. Modules
# # ---------- main.py ----------
# import example

# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
# result = example.area(3)

# print(result)

# # ---------- example.py ----------

# pi = 3.14159

# def square(x):
#    return x ** 2

# def cube(x):
#    return x ** 3

# def circumference(radius):
#    return 2 * pi * radius

# def area(radius):
#    return pi * radius ** 2


# # Lesson 40. Scope Resolution
# # ----- LOCAL -----

# def func1():
#     x = 1 #local
#     print(x)

# def func2():
#     x = 2 #local
#     print(x)

# func1()
# func2()

# # ----- ENCLOSED -----

# def func1():
#     x = 1 #enclosed

#     def func2():
#         print(x)
#     func2()

# func1()

# # ----- GLOBAL -----

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3 #global

# func1()
# func2()

# # ----- BUILT-IN -----

# from math import e 

# def func1():
#     print(e)

# func1()


# # Lesson 41. if_name_ == _main_
# #if __name__ == __main__: (this script can be imported OR run standalone)
# #Functions and classes in this module can be reused without the main block of code executing

# #Good practice (code is modular, helps readability, leaves no global variables, avoids unintended execution)

# # Ex. library = Import library for functionality.
# #                       When running library directly, display a help page

# # ---------- script1.py ----------
# # This file can run standalone or be imported

# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# def main():
#     print("This is script1")
#     favorite_food("pizza")
#     print("Goodbye!")

# if __name__ == '__main__':
#     main()

# # ---------- script2.py ----------
# # This file should run only standalone

# from script1 import *

# def favorite_drink(drink):
#     print(f"Your favorite drink is {drink}")

# print("This is script2")
# favorite_food("sushi")
# favorite_drink("coffee")
# print('Goodbye!')


# # Lesson 42. Credit Card Validator Program
# # Test Credit Card Account Numbers
# # American Express 378282246310005
# # American Express 371449635398431
# # American Express Corporate 378734493671000
# # Australian Bankcard 5610591081018250
# # Diners Club 30569309025904
# # Diners Club 38520000023237
# # Discover 6011111111111117
# # Discover 6011000990139424
# # JCB 3530111333300000
# # JCB 3566002020360505
# # MasterCard 5555555555554444
# # MasterCard 5105105105105100
# # Visa 4111111111111111
# # Visa 4012888888881881

# # Python credit card validator program

# # 1. Remove any '-' or ' '
# # 2. Add all digits in the odd places from right to left
# # 3. Double every second digit from right to left.
# #        (If result is a two-digit number,
# #        add the two-digit number together to get a single digit.)
# # 4. Sum the totals of steps 2 & 3
# # 5. If sum is divisible by 10, the credit card # is valid

# sum_odd_digits = 0
# sum_even_digits = 0
# total = 0

# # Step 1
# card_number = input("Enter a credit card #: ")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace(" ", "")
# card_number = card_number[::-1]

# # Step 2
# for x in card_number[::2]:
#     sum_odd_digits += int(x)

# # Step 3
# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits += x

# # Step 4
# total = sum_odd_digits + sum_even_digits

# # Step 5
# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")


# # Lesson 43. Banking Program
# # Python Banking Program

# def show_balance(balance):
#     print("*********************")
#     print(f"Your balance is ${balance:.2f}")
#     print("*********************")

# def deposit():
#     print("*********************")
#     amount = float(input("Enter an amount to be deposited: "))
#     print("*********************")
#     if amount < 0:
#         print("*********************")
#         print("That's not a valid amount")
#         print("*********************")
#         return 0
#     else:
#         return amount

# def withdraw(balance):
#     print("*********************")
#     amount = float(input("Enter amount to be withdrawn: "))
#     print("*********************")

#     if amount > balance:
#         print("*********************")
#         print("Insufficient funds")
#         print("*********************")
#         return 0
#     elif amount < 0:
#         print("*********************")
#         print("Amount must be greater than 0")
#         print("*********************")
#         return 0
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("*********************")
#         print("   Banking Program   ")
#         print("*********************")
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Exit")
#         print("*********************")
#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             show_balance(balance)
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -= withdraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("*********************")
#             print("That is not a valid choice")
#             print("*********************")

#     print("*********************")
#     print("Thank you! Have a nice day!")
#     print("*********************")

# if __name__ == '__main__':
#     main()


# # Lesson 44. Slot Machine
# # Python Slot Machine

# import random

# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

#     return [random.choice(symbols) for _ in range(3)]

# def print_row(row):
#     print("**************")
#     print(" | ".join(row))
#     print("**************")

# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 3
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '🍋':
#             return bet * 5
#         elif row[0] == '🔔':
#             return bet * 10
#         elif row[0] == '⭐':
#             return bet * 20
#     return 0

# def main():
#     balance = 100

#     print("*************************")
#     print("Welcome to Python Slots ")
#     print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
#     print("*************************")

#     while balance > 0:
#         print(f"Current balance: ${balance}")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Insufficient funds")
#             continue

#         if bet <= 0:
#             print("Bet must be greater than 0")
#             continue

#         balance -= bet

#         row = spin_row()
#         print("Spinning...\n")
#         print_row(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry you lost this round")

#         balance += payout

#         play_again = input("Do you want to spin again? (Y/N): ").upper()

#         if play_again != 'Y':
#             break

#     print("*******************************************")
#     print(f"Game over! Your final balance is ${balance}")
#     print("*******************************************")

# if __name__ == '__main__':
#     main()


# # Lesson 45. Hangman Game
# # Hangman in Python
# import random

# hangman_art = {0: ("   ",
#                                    "   ",
#                                    "   "),
#                              1: (" o ",
#                                    "   ",
#                                    "   "),
#                              2: (" o ",
#                                    " | ",
#                                    "   "),
#                              3: (" o ",
#                                    "/| ",
#                                    "   "),
#                              4: (" o ",
#                                   "/|\\",
#                                    "   "),
#                               5: (" o ",
#                                    "/|\\",
#                                    "/  "),
#                               6: (" o ",
#                                    "/|\\",
#                                    "/ \\")}

# words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

# def display_man(wrong_guesses):
#     print("**********")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("**********")

# def display_hint(hint):
#     print(" ".join(hint))

# def display_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue

#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue

#         guessed_letters.add(guess)

#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1

#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU LOSE!")
#             is_running = False

# if __name__ == "__main__":
#     main()


# # Lesson 46. Object Oriented Programming
# # --------------- car.py ---------------
# class Car:
#    def __init__(self, model, year, color, for_sale):
#        self.model = model
#        self.year = year
#        self.color = color
#        self.for_sale = for_sale

#    def drive(self):
#        # print("You drive the car")
#        # print(f"You drive the {self.model}")
#        print(f"You drive the {self.color} {self.model}")

#    def stop(self):
#        # print("You stop the car")
#        # print(f"You stop the {self.model}")
#        print(f"You stop the {self.color} {self.model}")

#    def describe(self):
#        print(f"{self.year} {self.color} {self.model}")
# # --------------------------------------
# # --------------- main.py ---------------
# from car import Car

# car1 = Car("Mustang", 2024, "red", False)
# car2 = Car("Corvette", 2025, "blue", True)
# car3 = Car("Charger", 2026, "yellow", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# car1.drive()
# car1.stop()
# car3.describe()

# # --------------------------------------


# # Lesson 47. Class Variables
# # class variables = Shared among all instances of a class
# #                               Defined outside the constructor
# #                               Allow you to share data among all objects created from that class

# class Student:

#    class_year = 2025
#    num_students = 0

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        Student.num_students += 1

# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student("Squidward", 55)
# student4 = Student("Sandy", 27)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)


# # Lesson 48. Inheritance
# # Inheritance = Allows a class to inherit attributes and methods from another class
# #                         Helps with code reusability and extensibility
# #                         class Child(Parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is asleep")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")


# # Lesson 49. Multiple Inheritance
# # multiple inheritance = inherit from more than one parent class
# #                                        C(A, B)

# # multilevel inheritance = inherit from a parent which inherits from another parent
# #                                          C(B) <- B(A) <- A

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")


# # Lesson 50. Abstract Classes
# # Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
# #                 They can contain abstract methods, which are declared but have no implementation.
# #                 Abstract classes benefits:
# #                 1. Prevents instantiation of the class itself
# #                 2. Requires children to use inherited abstract methods

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")

#     def stop(self):
#         print("You stop the car")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")

#     def stop(self):
#         print("You stop the motorcycle")

# class Boat(Vehicle):

#     def go(self):
#         print("You sail the boat")

#     def stop(self):
#         print("You anchor the boat")

# car = Car()
# motorcycle = Motorcycle()
# boat = Boat()


# # Lesson 51. super() 
# # super() = Function used in a child class to call methods from a parent class (superclass).
# #                  Allows you to extend the functionality of the inherited methods

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
#         super().describe()

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         print(f"It is a square with an area of {self.width * self.width}cm^2")
#         super().describe()

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
#         super().describe()

# circle = Circle(color="red", is_filled=True, radius=5)
# square = Square(color="blue", is_filled=False, width=6)
# triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

# circle.describe()
# square.describe()
# triangle.describe()



# # Lesson 52. Polymorphism
# # Polymorphism = Greek word that means to "have many forms or faces"
# #                               Poly = Many
# #                               Morphe = Form

# #                TWO WAYS TO ACHIEVE POLYMORPHISM
# #                1. Inheritance = An object could be treated of the same type as a parent class
# #                2. "Duck typing" = Object must have necessary attributes/methods

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")


# # Lesson 53. Duck Typing
#  "Duck typing" = Another way to achieve polymorphism besides Inheritance
# #                            Object must have the minimum necessary attributes/methods
# #                            "If it looks like a duck and quacks like a duck, it must be a duck."

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Car:
#     alive = True

#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


# # Lesson 54. Aggregation
# # Aggregation = Represents a relationship where one object (the whole)
# #                           Contains references to one or more INDEPENDENT objects (the parts)

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# library = Library("New York Public Library")

# book1 = Book("Harry Potter...", "J.K. Rowling")
# book2 = Book("The Hobbit", "J. R. R. Tolkein")
# book3 = Book("The Colour of Magic", "Terry Pratchett")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print(library.name)

# for book in library.list_books():
#     print(book)


# # Lesson 55. Composition
# # Aggregation = A relationship where one object contains references to other INDEPENDENT objects
# #                           "has-a" relationship

# # Composition = The composed object directly owns its components, which cannot exist independently
# #                            "owns-a" relationship

# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self, size):
#         self.size = size

# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

# car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
# car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

# print(car1.display_car())
# print(car2.display_car())


# # Lesson 56. Nested Classes
# # Nested class = A class defined within another class
# #                            class Outer:
# #                                class Inner:

# # Benefits: Allows you to logically group classes that are closely related
# #                 Encapsulates private details that aren't relevant outside of the outer class
# #                 Keeps the namespace clean; reduces the possibility of naming conflicts

# class Company:
#     class Employee:
#         def __init__(self, name, position):
#             self.name = name
#             self.position = position

#         def get_details(self):
#             return f"{self.name} {self.position}"

#     def __init__(self, company_name):
#         self.company_name = company_name
#         self.employees = []

#     def add_employee(self, name, position):
#         new_employee = self.Employee(name, position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         return [employee.get_details() for employee in self.employees]

# company1 = Company("Krusty Krab")
# company2 = Company("Chum Bucket")

# company1.add_employee("Eugene", "Manager")
# company1.add_employee("Spongebob", "Cook")
# company1.add_employee("Squidward", "Cashier")

# company2.add_employee("Sheldon", "Manager")
# company2.add_employee("Karen", "Assistant")

# for employee in company2.list_employees():
#     print(employee)


# # Lesson 57. Static Methods
# # Static methods = A method that belong to a class rather than any object from that class (instance)
# #                                Usually used for general utility functions

# # Instance methods - Best for operations on instances of the class (objects)
# # Static methods - Best for utility functions that do not need access to class data

# class Employee:

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     #INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name} = {self.position}"

#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions

# print(Employee.is_valid_position("Rocket Scientist"))


# # Lesson 58. Class Methods
# # Class methods = Allow operations related to the class
# #                                Take (cls) as the first parameter, which represents the class itself.

# #  Instance methods = Best for operations on instances of the class (objects)
# #  Static methods = Best for utility functions that do not need access to class data
# #  Class methods = Best for class-level data or require access to the class itself

# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     #INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name} {self.gpa}"

#     @classmethod
#     def get_count(cls):
#         return f"Total # of students: {cls.count}"

#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())


# # Lesson 59. Magic Methods
# # Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# #                                 They are automatically called by many of Python's built-in operations.
# #                                 They allow developers to define or customize the behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#         return self.num_pages > other.num_pages

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author

#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"Key '{key}' was not found"

# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
# book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book1)  # Calls __str__
# print(book1 == book3)  # Calls __eq__
# print(book1 < book2)  # Calls ___lt__
# print(book2 > book3)  # Calls __gt__
# print(book1 + book2)  # Calls __add__
# print("Lion" in book3)  # Calls __contains__
# print(book3['title'])  # Calls __getitem__


# # Lesson 60. Decorators
# # Decorator = A function that extends the behavior of another function
# #                      w/o modifying the base function
# #                      Pass the base function as an argument to the decorator

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You add sprinkles 🎊*")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("vanilla")


# # Lesson 61. @property
# # @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# #                        Benefit: Add additional logic when you read, write, or delete attributes
# #                        Gives you a getter, setter, and deleter method

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"

#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")

# rectangle = Rectangle(3, 4)


# # Lesson 62. Lambda
# # Lambda function = A small anonymous function for a one time use (throw away function)
# #                                    They take any number of arguments, but have only 1 expression
# #                                    Helps keep the namespace clean and is useful with higher-order functions
# #                                    'sort()', 'map()', 'filter()', 'reduce()'
# #                                    lambda parameters: expression

# double = lambda x: x * 2
# add = lambda x, y: x + y
# max_value = lambda x, y: x if x > y else y
# min_value = lambda x, y: x if x < y else y
# full_name = lambda first, last: first + " " + last
# is_even = lambda x: x % 2 == 0
# age_check = lambda age: True if age >= 18 else False

# print(double(2))
# print(add(3, 4))
# print(max_value(6, 7))
# print(min_value(9, 8))
# print(full_name("Spongebob", "Squarepants"))
# print(is_even(5))
# print(age_check(21))


# # Lesson 63. Sorting
# # SORTING IN PYTHON .sort() or sorted()
# # Lists[], Tuples(), Dictionaries{"":""}, Objects

# # ---------- LISTS ----------
# fruits = ["banana", "orange", "apple", "coconut"]

# # fruits.sort()
# # fruits.sort(reverse=True)

# print(fruits)

# # ---------- TUPLES ----------
# fruits = ("banana", "orange", "apple", "coconut")

# # fruits = tuple(sorted(fruits))
# # fruits = tuple(sorted(fruits, reverse=True))

# print(fruits)

# # ---------- DICTIONARIES ----------
# fruits = {
#    "banana": 105,
#    "apple": 72,
#    "orange": 73,
#    "coconut": 354
# }

# # fruits = dict(sorted(fruits.items()))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

# print(fruits)

# # ---------- OBJECTS ----------
# class Fruit:
#    def __init__(self, name, calories):
#        self.name = name
#        self.calories = calories

#    def __repr__(self):
#        return f"{self.name}: {self.calories}"

# fruits = [Fruit("banana", 105),
#               Fruit("apple", 72),
#               Fruit("orange", 73),
#               Fruit("coconut", 354)]

# # fruits = sorted(fruits, key=lambda fruit: fruit.name)
# # fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# # fruits = sorted(fruits, key=lambda fruit: fruit.calories)
# # fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

# print(fruits)


# # Lesson 64. zip()
# # zip() = Combines multiple iterables (lists, tuples, sets, dict)
# #             into a single iterator of tuples.
# #             Makes managing multiple indices easier.

# names = ["Spongebob", "Patrick", "Squidward"]
# ages = [30, 35, 50]
# jobs = ["Cook", "Unemployed", "Cashier"]

# data = zip(names, ages, jobs)

# for name, age, job in data:
#     print(f"{name} is a {age} year old {job}")


# # Lesson 65. Recursion
# # recursion = a function that calls itself from within
# #                      helps to visualize a complex problem into basic steps
# #                      problems can be solved more easily iteratively or recursively
# #                      iterative = faster, complex
# #                      recursive = slower, simpler

# # ----- EXAMPLE 1 -----

# # ITERATIVE
# def walk(steps):
#     for step in range(1, steps+1):
#         print(f"You take step #{step}")

# # RECURSIVE
# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps - 1)
#     print(f"You take step #{steps}")

# walk(100)

# # ----- EXAMPLE 2 -----

# # ITERATIVE
# def factorial(x):
#     result = 1
#     if x > 0:
#         for i in range(1, x + 1):
#             result *= i
#         return result

# # RECURSIVE
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)

# print(factorial(10))


# # Lesson 66. Exception Handling
# # exception = An event that interrupts the flow of a program
# #                     (ZeroDivisionError, TypeError, ValueError)
# #                     1.try, 2.except, 3.finally

# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You can't divide by zero IDIOT!")
# except ValueError:
#     print("Enter only numbers please!")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some cleanup here")


# # Lesson 67. File Detection
# # Python file detection

# import os

# file_path = "test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")


# # Lesson 68. Writing Files
# # Python writing files (.txt, .json, .csv)

# # --------- .txt ---------
# txt_data = "I like pizza!"

# file_path = "output.txt"

# try:
#    with open(file_path, 'w') as file:
#       file.write(txt_data)
#       print(f".txt file '{file_path}' has been created successfully")
# except FileExistsError:
#    print("That file already exists")

# # --------- .json ---------

# import json

# employee = {
#    "name": "Spongebob",
#    "age": 30,
#    "job": "Cook"
# }

# file_path = "output.json"

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employee, file, indent=4)

#     print(f"JSON file '{file_path}' has been created successfully")
# except FileExistsError:
#     print("That file already exists!")

# # --------- .csv---------
# import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]

# file_path = "output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# # Lesson 69. Read Files
# # Python reading files (.txt, .json, .csv)

# # ---------- .txt ----------

# file_path = "C:/Users/HP/Desktop/input.txt"

# try:
#   with open(file_path, 'r') as file:
#      content = file.read()
#      print(content)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")

# # ---------- .json ----------
# import json

# file_path = "C:/Users/HP/Desktop/input.json"

# try:
#   with open(file_path, 'r') as file:
#       content = json.load(file)
#       print(content )
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")

# # ---------- .csv ----------
# import csv

# file_path = "C:/Users/HP/Desktop/input.csv"

# try:
#   with open(file_path, 'r') as file:
#       content = csv.reader(file)
#       for line in content:
#           print(line)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")


# # Lesson 70. Execution Time
# # HOW TO MEASURE EXECUTION TIME IN PYTHON

# import time

# start_time = time.perf_counter()

# # YOUR CODE GOES HERE

# end_time = time.perf_counter()

# elapsed_time = end_time - start_time

# print(f"Elapsed time: {elapsed_time:.1f} seconds")


# # Lesson 71. Dates and Times
# import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()

# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()

# now = now.strftime("%H:%M:%S %m-%d-%Y")

# target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has NOT passed")


# # Lesson 72. Alarm Clock
# # Python Alarm Clock
# import time
# import datetime
# import pygame


# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "my_music.mp3"
#     is_running = True

#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)

#         if current_time == alarm_time:
#             print("WAKE UP! 😴")

#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)

#             is_running = False

#         time.sleep(1)


# if __name__ == "__main__":
#     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)


# # Lesson 73. Iterators
# # Iterator = An object that returns elements one at a time
# #                  from a sequence (or data stream)
# #                  and remembers its position between calls.
# #                  A Python object is an iterator if it has:
# #                 __iter__() → Returns the iterator object itself
# #                 __next__() → Returns the next item in the sequence
# #                                        (raises StopIteration when there's no more items)

# import random

# class Dice:
#     def __init__(self, rolls):
#         self.rolls = rolls
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < self.rolls:
#             self.count+=1
#             return random.randint(1, 6)
#         else:
#             raise StopIteration

# dice = Dice(3)

# for die in dice:
#     print(die)


# # Lesson 74. Generators
# # Generator = Function that behaves like an iterator (it can be used in a for loop)
# #                      Pauses a function, returns a value, then resumes
# #                      Uses 'yield' instead or 'return'
# #                      Iterate without loading everything into memory (ex. reading large files)
# #                      return = Pouring bucket
# #                      yield = Drip faucet

# # ---------- EXAMPLE 1 ----------

# def count_to(n):
#    count = 1
#    while count <= n:
#        yield count  # Pause here and return the current value
#        count += 1

# number = int(input("Enter a number to count up to: "))

# for n in count_to(number):
#    print(n)

# # ---------- EXAMPLE 2 ----------

# def read_file(file_path):
#    with open(file_path) as file:
#        for line in file:
#            yield line.strip()

# filepath = "C:\\Users\\HP\\Desktop\\test.txt"

# for line in read_file(filepath):
#    print(line)


# # Lesson 75. Generator Expressions
# # Generator Expression = Similar to a list comprehension but uses () instead of []
# #                                           Creates a generator (iterator) that yields values one at a time
# #                                           No need to define a function or use yield
# #                                           Less flexible than a gen func and not reusable
# #                                           gen object = (expression for value in iterable if condition)

# # ---------- EXAMPLE 1 ----------

# number = int(input("Enter a number to count up to: "))

# counter = (count for count in range(1, number + 1))

# for n in counter:
#    print(n)

# # ---------- EXAMPLE 2 ----------

# file_path = "C:\\Users\\HP\\Desktop\\test.txt"

# with open(file_path) as file:
#    lines = (line.strip() for line in file)
#    for line in lines:
#        print(line)

# # ---------- EXAMPLE 3 ----------

# number = int(input("Enter a number to square up to: "))

# even_squares = (x**2 for x in range(1, number + 1) if x % 2 == 0)

# for square in even_squares:
#    print(square)


# # Lesson 76. Data Classes
# # Data Class = A special kind of class that's designed mostly for holding data
# #                        without writing a lot of the boilerplate code for regular classes.
# #                        They automatically generate: _init__, __repr__, __eq_
# #                       (Python 3.7+)

# from dataclasses import dataclass, field

# @dataclass
# class Person:
#     name: str
#     age: int
#     password: str = field(repr=False)
#     is_alive: bool = True

#     def __post_init__(self):
#         if self.age < 0:
#             raise ValueError("Age cannot be negative")

# person1 = Person("Spongebob", 30, "pineapple1")
# person2 = Person("Patrick", 35, "password")

# print(person1)
# print(person2)
# print(person1 == person2)


# # Lesson 77. Multithreading
# # multithreading = Used to perform multiple tasks concurrently (multitasking)
# #                               Good for I/O bound tasks like reading files or fetching data from APIs

# import threading
# import time

# def walk_dog(first, last):
#    time.sleep(8)
#    print(f"You finish walking {first} {last}")

# def take_out_trash():
#    time.sleep(2)
#    print("You take out the trash")

# def get_mail():
#    time.sleep(4)
#    print("You get the mail")

# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # .join() ensures that all tasks are completed before proceeding
# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete!")


# # Lesson 78. Requesting API Data
# # https://pokeapi.co/
# #How to connect to an API using Python

# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "pikachu"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")




# # Lesson 79. PyQt5 Basic GUI Application
# # PyQt5 introduction
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My cool first GUI")
#         self.setGeometry(700, 300, 500, 500)
#         #self.setWindowIcon(QIcon("profile_pic.jpg"))

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":


# # Lesson 80. PyQt5 Labels
# # PyQt5 QLabels
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)

#         label = QLabel("Hello", self)
#         label.setFont(QFont("Arial", 40))
#         label.setGeometry(0, 0, 500, 100)
#         label.setStyleSheet("color: #292929;"
#                                            "background-color: #6fdcf7;"
#                                            "font-weight: bold;"
#                                            "font-style: italic;"
#                                            "text-decoration: underline;")

#         # label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
#         # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
#         # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

#         # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
#         # label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
#         # label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
#         # label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()


# # Lesson 81. PyQt5 Images
# # PyQt5 images
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QPixmap

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)

#         label = QLabel(self)
#         label.setGeometry(0, 0, 500, 500)

#         pixmap = QPixmap("profile_pic.jpg")
#         label.setPixmap(pixmap)

#         label.setScaledContents(True)

#         label.setGeometry((self.width() - label.width()) // 2,
#                                           (self.height() - label.height()) // 2,
#                                            label.width(),
#                                            label.height())

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if _name_ == "__main__":
#     main()


# # Lesson 82. PyQt5 Layout Managers
# # PyQt5 Layout Managers
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         label1 = QLabel("#1")
#         label2 = QLabel("#2")
#         label3 = QLabel("#3")
#         label4 = QLabel("#4")
#         label5 = QLabel("#5")

#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: blue;")
#         label5.setStyleSheet("background-color: purple;")

#         # VERTICAL LAYOUT
#         # -----------------
#         # vbox = QVBoxLayout()

#         # vbox.addWidget(label1)
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # vbox.addWidget(label5)

#         # central_widget.setLayout(vbox)

#         # HORIZONTAL LAYOUT
#         # -----------------
#         # hbox = QHBoxLayout()

#         # hbox.addWidget(label1)
#         # hbox.addWidget(label2)
#         # hbox.addWidget(label3)
#         # hbox.addWidget(label4)
#         # hbox.addWidget(label5)

#         # central_widget.setLayout(hbox)

#         # GRID LAYOUT
#         # -----------------
#         grid = QGridLayout()

#         grid.addWidget(label1, 0, 0)
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 1)
#         grid.addWidget(label5, 1, 2)

#         central_widget.setLayout(grid)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()


# # Lesson 83. Py Qt5 Buttons
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton("Click me!", self)
#         self.initUI()

#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)

#     def on_click(self):
#         print("Button clicked!")

# if _name_ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




# # Lesson 84. PyQt5 Checkboxes
# # PyQt5 Checkboxes
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.checkbox = QCheckBox("Do you like food?", self)
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setGeometry(10, 0, 500, 100)
#         self.checkbox.setStyleSheet("font-size: 50px;"
#                                                             "font-family: Arial;")
#         self.checkbox.stateChanged.connect(self.checkbox_changed)

#     def checkbox_changed(self, state):
#         if state == Qt.Checked:
#             print("You like food")
#         else:
#             print("You DO NOT like food")

# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    window = MainWindow()
#    window.show()
#    sys.exit(app.exec_())


# # Lesson 85. Py Qt5 Radio Buttons
# # PyQt5 radio buttons
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.radio1 = QRadioButton("Visa", self)
#         self.radio2 = QRadioButton("Mastercard", self)
#         self.radio3 = QRadioButton("Gift Card", self)
#         self.radio4 = QRadioButton("In-Store", self)
#         self.radio5 = QRadioButton("Online", self)
#         self.button_group1 = QButtonGroup(self)
#         self.button_group2 = QButtonGroup(self)
#         self.initUI()

#     def initUI(self):
#         self.radio1.setGeometry(0, 0, 300, 50)
#         self.radio2.setGeometry(0, 50, 300, 50)
#         self.radio3.setGeometry(0, 100, 300, 50)
#         self.radio4.setGeometry(0, 150, 300, 50)
#         self.radio5.setGeometry(0, 200, 300, 50)

#         self.setStyleSheet("QRadioButton{"
#                                          "font-size: 40px;"
#                                          "font-family: Arial;"
#                                          "padding: 10px;"
#                                          "}")

#         self.button_group1.addButton(self.radio1)
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)
#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)

#         self.radio1.toggled.connect(self.radio_button_changed)
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)

#     def radio_button_changed(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")

# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   window = MainWindow()
#   window.show()
#   sys.exit(app.exec_())

# # Lesson 86. PyQt5 Line Edits
# # PyQt5 LineEdit
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.line_edit = QLineEdit(self)
#         self.button = QPushButton("Submit", self)
#         self.initUI()

#     def initUI(self):
#         self.line_edit.setGeometry(10, 10, 200, 40)
#         self.button.setGeometry(210, 10, 100, 40)
#         self.line_edit.setStyleSheet("font-size: 25px;"
#                                                          "font-family: Arial")
#         self.button.setStyleSheet("font-size: 25px;"
#                                                       "font-family: Arial")
#         self.line_edit.setPlaceholderText("Enter your name")

#         self.button.clicked.connect(self.submit)

#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Hello {text}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# # Lesson 87. PyQt5 Add CSS to Python
# # PyQt5 setStyleSheet()
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.button1 = QPushButton("#1")
#         self.button2 = QPushButton("#2")
#         self.button3 = QPushButton("#3")
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         hbox = QHBoxLayout()

#         hbox.addWidget(self.button1)
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)

#         central_widget.setLayout(hbox)

#         self.button1.setObjectName("button1")
#         self.button2.setObjectName("button2")
#         self.button3.setObjectName("button3")

#         self.setStyleSheet("""
#             QPushButton{
#                 font-size: 40px;
#                 font-family: Arial;
#                 padding: 15px 75px;
#                 margin: 25px;
#                 border: 3px solid;
#                 border-radius: 15px;
#             }
#             QPushButton#button1{
#                 background-color: hsl(0, 100%, 64%);
#             }
#             QPushButton#button2{
#                 background-color: hsl(122, 100%, 64%);
#             }
#             QPushButton#button3{
#                 background-color: hsl(204, 100%, 64%);
#             }
#             QPushButton#button1:hover{
#                 background-color: hsl(0, 100%, 84%);
#             }
#             QPushButton#button2:hover{
#                 background-color: hsl(122, 100%, 84%);
#             }
#             QPushButton#button3:hover{
#                 background-color: hsl(204, 100%, 84%);
#             }
#         """)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# # Lesson 88. Digital Clock
# # Python PyQt5 Digital Clock
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import QTimer, QTime, Qt
# from PyQt5.QtGui import QFont, QFontDatabase

# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Digital Clock")
#         self.setGeometry(600, 400, 300, 100)

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)

#         self.time_label.setAlignment(Qt.AlignCenter)

#         self.time_label.setStyleSheet("font-size: 150px;"
#                                                              "color: hsl(111, 100%, 50%);")
#         self.setStyleSheet("background-color: black;")

#         # Use a custom font
#         # font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
#         # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         # my_font = QFont(font_family, 150)
#         # self.time_label.setFont(my_font)

#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)

#         self.update_time()

#     def update_time(self):
#         current_time = QTime.currentTime().toString("hh:mm:ss AP")
#         self.time_label.setText(current_time)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())


# # Lesson 89. Stopwatch
# # Python PyQt5 Stopwatch
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
#                                                        QPushButton, QVBoxLayout, QHBoxLayout)
# from PyQt5.QtCore import QTimer, QTime, Qt

# class Stopwatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label = QLabel("00:00:00.00", self)
#         self.start_button = QPushButton("Start", self)
#         self.stop_button = QPushButton("Stop", self)
#         self.reset_button = QPushButton("Reset", self)
#         self.timer = QTimer(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Stopwatch")

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)

#         self.setLayout(vbox)

#         self.time_label.setAlignment(Qt.AlignCenter)

#         hbox = QHBoxLayout()

#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox)

#         self.setStyleSheet("""
#             QPushButton, QLabel{
#                 padding: 20px;
#                 font-weight: bold;
#                 font-family: calibri;
#             }
#             QPushButton{
#                 font-size: 50px;
#             }
#             QLabel{
#                 font-size: 120px;
#                 background-color: hsl(200, 100%, 85%);
#                 border-radius: 20px;
#             }
#         """)

#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)

#     def start(self):
#         self.timer.start(10)

#     def stop(self):
#         self.timer.stop()

#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label.setText(self.format_time(self.time))

#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         milliseconds = time.msec() // 10
#         return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     stopwatch = Stopwatch()
#     stopwatch.show()
#     sys.exit(app.exec_())


# # Lesson 90. Weather App
# # https://openweathermap.org/

# import sys
# import requests
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
#                                                        QLineEdit, QPushButton, QVBoxLayout)
# from PyQt5.QtCore import Qt

# class WeatherApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.city_label = QLabel("Enter city name: ", self)
#         self.city_input = QLineEdit(self)
#         self.get_weather_button = QPushButton("Get Weather", self)
#         self.temperature_label = QLabel(self)
#         self.emoji_label = QLabel(self)
#         self.description_label = QLabel(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Weather App")

#         vbox = QVBoxLayout()

#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperature_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)

#         self.setLayout(vbox)

#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)

#         self.city_label.setObjectName("city_label")
#         self.city_input.setObjectName("city_input")
#         self.get_weather_button.setObjectName("get_weather_button")
#         self.temperature_label.setObjectName("temperature_label")
#         self.emoji_label.setObjectName("emoji_label")
#         self.description_label.setObjectName("description_label")

#         self.setStyleSheet("""
#             QLabel, QPushButton{
#                 font-family: calibri;
#             }
#             QLabel#city_label{
#                 font-size: 40px;
#                 font-style: italic;
#             }
#             QLineEdit#city_input{
#                 font-size: 40px;
#             }
#             QPushButton#get_weather_button{
#                 font-size: 30px;
#                 font-weight: bold;
#             }
#             QLabel#temperature_label{
#                 font-size: 75px;
#             }
#             QLabel#emoji_label{
#                 font-size: 100px;
#                 font-family: Segoe UI emoji;
#             }
#             QLabel#description_label{
#                 font-size: 50px;
#             }
#         """)

#         self.get_weather_button.clicked.connect(self.get_weather)

#     def get_weather(self):

#         api_key = "YOUR API KEY GOES HERE"
#         city = self.city_input.text()
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             data = response.json()

#             if data["cod"] == 200:
#                 self.display_weather(data)

#         except requests.exceptions.HTTPError as http_error:
#             match response.status_code:
#                 case 400:
#                     self.display_error("Bad request:\nPlease check your input")
#                 case 401:
#                     self.display_error("Unauthorized:\nInvalid API key")
#                 case 403:
#                     self.display_error("Forbidden:\nAccess is denied")
#                 case 404:
#                     self.display_error("Not found:\nCity not found")
#                 case 500:
#                     self.display_error("Internal Server Error:\nPlease try again later")
#                 case 502:
#                     self.display_error("Bad Gateway:\nInvalid response from the server")
#                 case 503:
#                     self.display_error("Service Unavailable:\nServer is down")
#                 case 504:
#                     self.display_error("Gateway Timeout:\nNo response from the server")
#                 case _:
#                     self.display_error(f"HTTP error occurred:\n{http_error}")

#         except requests.exceptions.ConnectionError:
#             self.display_error("Connection Error:\nCheck your internet connection")
#         except requests.exceptions.Timeout:
#             self.display_error("Timeout Error:\nThe request timed out")
#         except requests.exceptions.TooManyRedirects:
#             self.display_error("Too many Redirects:\nCheck the URL")
#         except requests.exceptions.RequestException as req_error:
#             self.display_error(f"Request Error:\n{req_error}")

#     def display_error(self, message):
#         self.temperature_label.setStyleSheet("font-size: 30px;")
#         self.temperature_label.setText(message)
#         self.emoji_label.clear()
#         self.description_label.clear()

#     def display_weather(self, data):
#         self.temperature_label.setStyleSheet("font-size: 75px;")
#         temperature_k = data["main"]["temp"]
#         temperature_c = temperature_k - 273.15
#         temperature_f = (temperature_k * 9/5) - 459.67
#         weather_id = data["weather"][0]["id"]
#         weather_description = data["weather"][0]["description"]

#         self.temperature_label.setText(f"{temperature_f:.0f}°F")
#         self.emoji_label.setText(self.get_weather_emoji(weather_id))
#         self.description_label.setText(weather_description)

#     @staticmethod
#     def get_weather_emoji(weather_id):

#         if 200 <= weather_id <= 232:
#             return "⛈"
#         elif 300 <= weather_id <= 321:
#             return "🌦"
#         elif 500 <= weather_id <= 531:
#             return "🌧"
#         elif 600 <= weather_id <= 622:
#             return "❄"
#         elif 701 <= weather_id <= 741:
#             return "🌫"
#         elif weather_id == 762:
#             return "🌋"
#         elif weather_id == 771:
#             return "💨"
#         elif weather_id == 781:
#             return "🌪"
#         elif weather_id == 800:
#             return "☀"
#         elif 801 <= weather_id <= 804:
#             return "☁"
#         else:
#             return ""

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     weather_app = WeatherApp()
#     weather_app.show()
#     sys.exit(app.exec_())


# # Lesson 91. QR Code
# # In a terminal: pip install qrcode[pil]
# import qrcode

# url = input("Enter the URL: ").strip()
# file_path = "qrcode.png"

# qr = qrcode.QRCode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)

# print("QR Code was generated!")


# # Lesson 92. Music Player
# import os
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
# import pygame

# def play_music(folder, song_name):

#     file_path = os.path.join(folder, song_name)

#     if not os.path.exists(file_path):
#         print("File not found")
#         return

#     pygame.mixer.music.load(file_path)
#     pygame.mixer.music.play()

#     print(f"\nNow playing: {song_name}")
#     print("Commands: [P]ause, [R]esume, [S]top")

#     while True:

#         command = input("> ").upper()

#         if command == "P":
#             pygame.mixer.music.pause()
#             print("Paused")
#         elif command == "R":
#             pygame.mixer.music.unpause()
#             print("Resumed")
#         elif command == "S":
#             pygame.mixer.music.stop()
#             print("Stopped")
#             return
#         else:
#             print("Invalid command")

# def main():

#     try:
#         pygame.mixer.init()
#     except pygame.error as e:
#         print("Audio initialization failed! ", e)
#         return

#     folder = "music"

#     if not os.path.isdir(folder):
#         print(f"Folder '{folder}' not found")
#         return

#     mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

#     if not mp3_files:
#         print("No .mp3 files found!")

#     while True:
#         print("*** MP3 PLAYER *****")
#         print("My song list:")

#         for index, song in enumerate(mp3_files, start=1):
#             print(f"{index}. {song}")

#         choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

#         if choice_input.upper() == "Q":
#             print("Bye!")
#             break

#         if not choice_input.isdigit():
#             print("Enter a valid number")
#             continue

#         choice = int(choice_input) - 1

#         if 0 <= choice < len(mp3_files):
#             play_music(folder, mp3_files[choice])
#         else:
#             print("Invalid choice")

# if _name_ == "__main__":
#     main()


