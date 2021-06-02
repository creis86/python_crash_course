# Python Crash Course by Eric Matthes
# Chapter 06: Dictionaries

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-1
# person_0 = {
#     'first_name': 'thereza',
#     'last_name': 'souza',
#     'age': 64,
#     'city': 'recife',
#     }

# print(person_0['first_name'].title())
# print(person_0['last_name'].title())
# print(person_0['age'])
# print(person_0['city'].title())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-3
# glossary = {
#     'append': 'method that adds an element to the end of a list',
#     'del': 'function that removes an element of a list or dictionary',
#     'for': 'command used for looping through lists or blocks of code',
#     'range': 'specifies a range of numbers which is useful for looping',
#     'upper': 'used to convert a string to uppercase',
#     }

# print(f"append:\n\t{glossary['append']}\n")
# print(f"del:\n\t{glossary['del']}\n")
# print(f"for:\n\t{glossary['for']}\n")
# print(f"range:\n\t{glossary['range']}\n")
# print(f"upper:\n\t{glossary['upper']}\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-4
# for keyword, meaning in glossary.items():
#     print(f"{keyword}:\n\t{meaning}\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-5
# river_locations = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china',
#     'mississippi': 'united states',
#     'yellow': 'china',
#     }

# for river, country in river_locations.items():
#     print(f"The {river.title()} river runs through {country.title()}.")
# print("\n")

# for river in river_locations.keys():
#     print(f"{river.title()}")
# print("\n")

# for country in river_locations.values():
#     print(f"{country.title()}")
# print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-6
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# poll_candidates = ['sarah', 'robert', 'john', 'phil', 'megan']

# for name in sorted(poll_candidates):
#     if name in favorite_languages.keys():
#         print(f"Thank you for responding, {name.title()}!")
#     else:
#         print(f"You should take the poll, {name.title()}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-7
# person_0 = {
#     'first_name': 'carlos',
#     'last_name': 'reis',
#     'age': 34,
#     }

# person_1 = {
#     'first_name': 'thereza',
#     'last_name': 'souza',
#     'age': 64,
#     }

# person_2 = {
#     'first_name': 'rianna',
#     'last_name': 'ramos',
#     'age': 30,
#     }

# people = [person_0, person_1, person_2]

# for person in people:
#     full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = f"{person['age']}"

#     print(full_name)
#     print(f"{age}\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-9
# favorite_places = {
#     'carlos': ['itamaracá', 'jaqueira'],
#     'thereza': ['bompreço', 'banco', 'farmácia'],
#     'rianna': ['garanhuns']
#     }

# for person, places in favorite_places.items():
#     if len(places) <= 1:
#         print(f"{person.title()}'s favorite place is:"
#             f"\n\t{places[0].title()}\n")

#     else:
#         print(f"{person.title()}'s favorite places are:")
#         for place in places:
#             print(f"\t{place.title()}")
#         print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-10
# favorite_numbers = {
#     'carlos': [16, 9, 86],
#     'thereza': [7, 57],
#     'rianna': [11, 5],
#     }

# for name, numbers in favorite_numbers.items():
#     print(f"{name.title()}'s favorite numbers are:")
#     print(*numbers, sep = ", ")
#     print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 6-11
# cities = {
#     'caruaru': {
#         'country': 'Brazil',
#         'population': 370_000,
#         'fact': "known for some great quality forró",
#         },

#     'hollywood': {
#         'country': 'United States',
#         'population': 155_000,
#         'fact': "its famous sign is almost 90 years old",
#         },

#     'paris': {
#         'country': 'France',
#         'population': 2_000_000,
#         'fact': 'home of the Eiffel Tower and the Louvre Museum',
#         },
#     }

# for city, city_data in cities.items():
#     print(f"{city.title()} data:")

#     for info, info_value in city_data.items():
#         print(f"\t{info.title()}: {info_value}")

#     print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *