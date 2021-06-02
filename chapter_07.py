# Python Crash Course by Eric Matthes
# Chapter 07: User input and while loops

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-1
# car = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a {car.title()}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-2
# group_size = input("How many people are there in your dinner group? ")
# group_size = int(group_size)

# if group_size > 8:
#     print("Sorry, you'll need to wait for a table.")
# else:
#     print("Your table is ready.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-3
# prompt = "I can check if a number is multiple of 10."
# prompt += "\nWrite a number: "

# number = input(prompt)
# number = int(number)

# if number % 10 == 0:
#     print(f"{number} is multiple of 10.")
# else:
#     print(f"{number} is not multiple of 10.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-4
# prompt = "Select a topping:"
# prompt += "\n(Type 'quit' to finish choosing.) "

# while True:
#     topping = input(prompt)

#     if topping == "quit":
#         break
#     else:
#         print(f"We'll add {topping} to ypur pizza.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-5
# while True:
#     age = input("How old are you? ")

#     if age == "quit":
#         break
#     else:
#         age = int(age)

#         if age < 3:
#             print("Your ticket is free of charge.")
#         elif age < 12:
#             print("Your ticket costs $10.")
#         else:
#             print("Your ticket costs $15.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-9
# sandwich_orders = ["pastrami", "cheddar", "pastrami",
#                    "big tasty", "mc supreme", "pastrami"]
# finished_sandwiches = []

# print("Sorry, we ran out of Pastrami sandwiches.")

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(current_sandwich)

#     print(f"I made your {current_sandwich.title()} sandwich.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 7-10
# poll_active = True
# poll_results = {}

# while poll_active:
#     name = input("What's your name? ")
#     response = input ("If you could visit one place in the world, " +
#                       "where would you go? ")
#     poll_results[name] = response

#     repeat = input("Would you like to let another person respond? (y/n) ")
#     if repeat == "n":
#         poll_active = False

# print("\n----- Poll Results -----")
# for name, response in poll_results.items():
#     print(f"{name.title()} would like to visit {response.title()}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *