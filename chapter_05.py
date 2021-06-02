# Python Crash Course by Eric Matthes
# Chapter 05: If statements

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-1
# car = 'crossfox'

# print("Is car == 'Crossfox'? I predict False.")
# print(car == 'Crossfox')

# print("\nIs car == 'BMW'? I predict False.")
# print(car == 'BMW')

# print("\nIs car == 'crossfox'? I predict True.")
# print(car == 'crossfox')

# plane = 'bOeiNG'

# print("\nIs plane == 'Boeing'? I predict True.")
# print(plane.title() == 'Boeing')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-2
# group_members = ['André', 'Bianca', 'Camila']
# is_a_member   = False

# print("Is Carlos in the group? I predict False.")
# for person in group_members:
#     if person.lower() == 'carlos':
#         is_a_member = True
# print(f"{is_a_member}\n")

# print("Is André in the group? I predict True.")
# for person in group_members:
#     if person.lower() == 'andré':
#         is_a_member = True
# print(f"{is_a_member}\n")

# print("Is Bianca in the group? I predict True.")
# if 'Bianca' in group_members:
#     print("True\n")
# if 'Bianca' not in group_members:
#     print("False\n")

# print("Are both Bianca and Carlos in the group? I predict False.")
# if ('Bianca' in group_members) and ('Carlos' in group_members):
#     print("True\n")
# if ('Bianca' not in group_members) or ('Carlos' not in group_members):
#     print("False\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-5
# alien_color = 'yellow'

# if alien_color == 'green':
#     print("You earned 5 points.")
# elif alien_color == 'yellow':
#     print("You earned 10 points.")
# elif alien_color == 'red':
#     print("You earned 15 points.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-6
# age = 34

# if age < 2:
#     stage_of_life = "baby"
# elif age < 4:
#     stage_of_life = "toddler"
# elif age < 13:
#     stage_of_life = "kid"
# elif age < 20:
#     stage_of_life = "teenager"
# elif age < 65:
#     stage_of_life = "adult"
# else:
#     stage_of_life = "elder"

# if (stage_of_life == 'adult') or (stage_of_life == 'elder'):
#     print(f"This person is an {stage_of_life}.")
# else:
#     print(f"This person is a {stage_of_life}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-7
# favorite_fruits = ['apple', 'grape', 'pineapple', 'strawberry']

# if 'grape' in favorite_fruits:
#     print("You really like grapes!")

# if 'banana' in favorite_fruits:
#     print("You really like bananas!")

# if 'avocado' in favorite_fruits:
#     print("You really like avocados!")

# if 'apple' in favorite_fruits:
#     print("You really like apples!")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-9
# usernames = ['carlos', 'thereza', 'admin', 'lucas']

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello, admin. Would you like to see a status report?")
#         else:
#             print(f"Hello, {username.title()}. Thanks for logging in again.")
# else:
#     print("We need to find some users!")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 5-10
# current_users      = ['aUgUsto', 'br3n0', 'Cibele', 'DANIEL']
# current_users_copy = []
# new_users          = ['Augusto', 'BrUn0', 'CIBELE', 'danilo']

# for index in range(0, len(current_users)):
#     current_users_copy.append(current_users[index].lower())

# for new_user in new_users:
#     available_name = True

#     for current_user in current_users_copy:
#         if new_user.lower() == current_user:
#             available_name = False

#     if available_name:
#         print(f"{new_user}, this username is available.")
#     else:
#         print(f"{new_user}, this username has been taken. Choose a new one.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *