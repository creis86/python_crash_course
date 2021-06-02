# Python Crash Course by Eric Matthes
# Chapter 10: Files and exceptions

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-1
# file_path = 'text_files/learning_python.txt'

#///////////////////////////////////////////////////////////////////////////////
#/ Reading the entire file
#///////////////////////////////////////////////////////////////////////////////
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

#///////////////////////////////////////////////////////////////////////////////
#/ Looping through the file object
#///////////////////////////////////////////////////////////////////////////////
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#///////////////////////////////////////////////////////////////////////////////
#/ Storing lines in a list
#///////////////////////////////////////////////////////////////////////////////
# with open(file_path) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-2
# file_path = 'text_files/learning_python.txt'
# with open(file_path) as file_object:
#     for line in file_object:
#         modified_line = line.replace('Python', 'Java')
#         print(line.rstrip())
#         print(modified_line)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-4
# with open('text_files/guest_book.txt', 'a') as file_object:
#     guest_name = ''
#     while True:
#         guest_name = input("Enter your name: ").title()
#         if guest_name == 'Q':
#             break
#         print(f"Hello, {guest_name}!\n")
#         file_object.write(f"{guest_name}\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-6
# print("\nGive me two integers and I'll add them.")
# first_number = input("First number: ")
# try:
#     first_number = int(first_number)
# except ValueError:
#     print("\nInvalid input.")
# else:
#     second_number = input("Second number: ")
#     try:
#         second_number = int(second_number)
#     except ValueError:
#         print("\nInvalid input.")
#     else:
#         result = first_number + second_number
#         print(f"The result is {result}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-7
# def get_retry_choice():
#     """
#     Prompts the user whether he wants to retry an operation or not.
#     Returns a choice_char which is equal to either 'y' or 'n'.
#     """
#     choice_char = ''
#     while choice_char != 'y' and choice_char != 'n':
#         choice_char = input("Would you like to try again? (y/n): ")
#     return choice_char


# while True:
#     print("\nGive me two integers and I'll add them.")
#     first_number = input("First number: ")
#     try:
#         first_number = int(first_number)
#     except ValueError:
#         print("\nInvalid input. Enter an integer value.")
#         retry = get_retry_choice()
#         if retry == 'y':
#             continue
#         else:
#             break
#     else:
#         second_number = input("Second number: ")
#         try:
#             second_number = int(second_number)
#         except ValueError:
#             print("\nInvalid input. Enter an integer value.")
#             retry = get_retry_choice()
#             if retry == 'y':
#                 continue
#             else:
#                 break
#         else:
#             result = first_number + second_number
#             print(f"{result}\n")
#             retry = get_retry_choice()
#             if retry == 'n':
#                 break

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-8
# files = ['text_files/cats.txt', 'text_files/dogs.txt']
# for file in files:
#     try:
#         with open(file) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print(f"File not found: '{file}'.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-10
# filename = 'text_files/Moby-Dick; or The Whale.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
#         print(contents.lower().count('the'))
#         print(contents.lower().count('the '))
# except FileNotFoundError:
#     pass

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-11
#///////////////////////////////////////////////////////////////////////////////
#/ Writing program
#///////////////////////////////////////////////////////////////////////////////
# import json

# number = input("What's your favorite number? ")
# filename = 'json_files/favorite_number.json'
# with open(filename, 'w') as f:
#     json.dump(number, f)

#///////////////////////////////////////////////////////////////////////////////
#/ Reading program
#///////////////////////////////////////////////////////////////////////////////
# import json

# filename = 'json_files/favorite_number.json'
# try:
#     with open(filename) as f:
#         number = json.load(f)
# except FileNotFoundError:
#     print(f"File not found: '{filename}'.")
# else:
#     print(f"I know your favorite number! It's {number}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-12
# import json

# filename = 'json_files/favorite_number.json'
# try:    
#     with open(filename) as f:
#         number = json.load(f)
#         print(f"I know your favorite number! It's {number}.")
# except FileNotFoundError:
#     with open(filename, 'w') as f:
#         number = input("What's your favorite number? ")
#         json.dump(number, f)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 10-13
# import json

# def get_stored_username():
#     """
#     Retrieves stored username, if available.
#     """
#     filename = 'json_files/username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username


# def get_new_username():
#     """
#     Prompts the user for a new username.
#     """
#     username = input("What's your name? ")
#     filename = 'json_files/username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username


# def confirm_username(username):
#     """
#     Asks the user to confirm his username.
#     """
#     answer = ''
#     while answer != 'y' and answer != 'n':
#         answer = input(f"Are you {username}? (y/n): ")
#     if answer == 'y':
#         return True
#     else:
#         return False


# def greet_user():
#     """
#     Greets the user by name.
#     """
#     username = get_stored_username()
#     if username:
#         if confirm_username(username):
#             print(f"Welcome back, {username}!")
#         else:
#             username = get_new_username()
#             print(f"Nice to meet you, {username}!")
#     else:
#         username = get_new_username()
#         print(f"Nice to meet you, {username}!")


# greet_user()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *