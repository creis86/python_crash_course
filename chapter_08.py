# Python Crash Course by Eric Matthes
# Chapter 08: Functions

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-1
# def display_message():
#     """Displays a message about the subject of this chapter."""
#     print("I'm studying functions in Python.")

# display_message()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-2
# def favorite_book(book_title):
#     """Prints a message about my favorite book."""
#     print(f"My favorite book is {book_title.title()}.")

# favorite_book("python crash course")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-3
# def make_shirt(size, text):
#     """Prints a sentence about a shirt's size and text."""
#     print(f"I have a {size} size T-shirt.")
#     print(f"It has the following text: '{text}'.")

# make_shirt("M", "Hello World")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-4
# def make_shirt(size = "L", text = "I love Python"):
#     """Prints a sentence about a shirt's size and text."""
#     print(f"I have a {size} size T-shirt.")
#     print(f"It has the following text: '{text}'.")

# make_shirt()
# print("\n")

# make_shirt("M")
# print("\n")

# make_shirt("S", "Hello World")
# print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-5
# def describe_city(city_name, country = "Brasil"):
#     print(f"{city_name.title()} is located in {country.title()}.")

# describe_city("recife")
# describe_city("new york", "united states")
# describe_city(city_name = "osaka", country = "japan")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-6
# def city_country(city, country):
#     return f"{city.title()}, {country.title()}"

# city_1 = city_country("recife", "brasil")
# city_2 = city_country("santiago", "chile")
# city_3 = city_country("san francisco", "united states")

# print(city_1)
# print(city_2)
# print(city_3)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-7
# def make_album(artist_name, album_title, number_of_songs = None):
#     album = {
#             'artist': artist_name.title(),
#             'title': album_title.title(),}

#     if number_of_songs:
#         album['songs'] = number_of_songs

#     return album

# album_1 = make_album("red hot chili peppers", "californication", 16)
# album_2 = make_album("the beatles", "let it be", 12)
# album_3 = make_album("tim maia", "racional, vol. 1")

# print(album_1)
# print(album_2)
# print(album_3)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-8
# while True:
#     print("Insira as informações sobre o álbum.")
#     print("(digite 'q' e pressione ENTER para finalizar a qualquer momento)\n")

#     artist = input("Artista: ")
#     if artist == 'q':
#         break

#     title = input("Título: ")
#     if title == 'q':
#         break

#     album = make_album(artist, title)
#     print(album)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-9
# message_list = ["Hello World!", "I love Python!", "To be, or not to be?"]

# def show_messages(messages):
#     while messages:
#         current_msg = messages.pop(0)
#         print(current_msg)

# show_messages(message_list)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-10
# def send_messages(unsent_messages, sent_messages):
#     while unsent_messages:
#         current_msg = unsent_messages.pop(0)
#         print(current_msg)
#         sent_messages.append(current_msg)

# sent_messages = []
# send_messages(message_list, sent_messages)

# print(message_list)
# print(sent_messages)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-11
# send_messages(message_list[:], sent_messages)

# print(message_list)
# print(sent_messages)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-12
# def sandwich_summary(*items):
#     print("\nThe ordered sandwich has the following items:")

#     for item in items:
#         print(f"- {item}")

# sandwich_summary('cheese')
# sandwich_summary('cheese', 'egg')
# sandwich_summary('cheese', 'egg', 'bacon')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-13
# def build_profile(first, last, **user_info):
#     """
#     Builds a dictionary containing everything we know about a user.
#     """
#     user_info['f_name'] = first
#     user_info['l_name'] = last
#     return user_info

# my_profile = build_profile('Carlos', 'Reis', gender='M', age=34, height=1.78)
# print(my_profile)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-14
# def car_data(manufacturer, model, **kwargs):
#     kwargs['manufacturer'] = manufacturer
#     kwargs['model'] = model
#     return kwargs

# my_car_summary = car_data('wolkswagen', 'crossfox',\
#                           color='grey', insurance=True)
# print(my_car_summary)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-15
# import my_module as m

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# finished_models = []

# m.print_models(unprinted_designs, finished_models)
# m.show_completed_models(finished_models)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 8-16
# from my_module import print_models, show_completed_models

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# finished_models = []

# print_models(unprinted_designs, finished_models)
# show_completed_models(finished_models)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *