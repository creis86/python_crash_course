# Python Crash Course by Eric Matthes
# Chapter 03: Introducing lists

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-1
# names = ['alberto', 'bruno', 'carlos']
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-2
# print(f"How are you, {names[0]}?")
# print(f"How are you, {names[1]}?")
# print(f"How are you, {names[2]}?"

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-3
# vehicles = ['airplane', 'bus', 'car']
# print(f"I've never traveled by {vehicles[0]}.")
# print(f"Traveling by {vehicles[1]} is a pain!")
# print(f"I own a {vehicles[2]}.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-4
# guests = ['maria augusta', 'rianna', 'thereza']
# print(f"{guests[0].title()}, vamos jantar fora?")
# print(f"{guests[1].title()}, vamos jantar fora?")
# print(f"{guests[2].title()}, vamos jantar fora?")
# print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-5
# print(f"{guests[0].title()} não irá comparecer.\n")

# guests[0] = 'lucas'
# print(f"{guests[0].title()}, vamos jantar fora?")
# print(f"{guests[1].title()}, vamos jantar fora?")
# print(f"{guests[2].title()}, vamos jantar fora?")
# print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-6
# guests.insert(0, 'alessandra')
# guests.insert(1, 'elaine')
# guests.append('zilma')
# print(f"{guests[0].title()}, vamos jantar fora?")
# print(f"{guests[1].title()}, vamos jantar fora?")
# print(f"{guests[2].title()}, vamos jantar fora?")
# print(f"{guests[3].title()}, vamos jantar fora?")
# print(f"{guests[4].title()}, vamos jantar fora?")
# print(f"{guests[5].title()}, vamos jantar fora?")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

#Exercise 3-7
# print("Só há lugar para dois convidados...\n")

# cancelled = 'alessandra'
# guests.remove(cancelled)
# print(f"Desculpe, {cancelled.title()}!")

# cancelled = 'elaine'
# guests.remove(cancelled)
# print(f"Desculpe, {cancelled.title()}!")

# cancelled = 'lucas'
# guests.remove(cancelled)
# print(f"Desculpe, {cancelled.title()}!")

# cancelled = 'zilma'
# guests.remove(cancelled)
# print(f"Desculpe, {cancelled.title()}!")

# del guests[0]
# del guests[0]
# print(guests)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-8
# locations = ['japan', 'hawaii', 'france', 'dubai', 'thailand']
# print(f"{locations}\n")

# print(sorted(locations))
# print(f"{locations}\n")

# print(sorted(locations, reverse = True))
# print(f"{locations}\n")

# locations.reverse()
# print(f"{locations}\n")

# locations.sort()
# print(f"{locations}\n")

# locations.sort(reverse = True)
# print(f"{locations}\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 3-9
# print(f"Há {len(guests)} convidados na lista.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *