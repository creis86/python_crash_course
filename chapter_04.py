# Python Crash Course by Eric Matthes
# Chapter 04: Working with lists

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-1
# pizza_flavors = ['margherita', 'mozzarella', 'pepperoni']

# for flavor in pizza_flavors:
#     print(f"I like {flavor} pizza.")

# print("I really love pizza.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-2
# animals = ['cat', 'dog', 'hamster']

# for animal in animals:
#     print(f'A {animal} would make a great pet.')

# print('Any of these animals would make a great pet.')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-3
# for number in range(1, 21):
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-4
# number_list = [number for number in range(1, 1_000_001)]

# for number in number_list:
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-5
# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-6
# odd_numbers = []

# for number in range(1, 20, 2):
#     odd_numbers.append(number)

# for number in odd_numbers:
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-7
# multiples_of_3 = [number for number in range(3, 31, 3)]

# for number in multiples_of_3:
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-8
# cubes = []

# for number in range(1, 11):
#     cubes.append(number**3)

# for number in cubes:
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-9
# cubes = [number**3 for number in range (1, 11)]

# for number in cubes:
#     print(number)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-10
# letters = ['a', 'b', 'c', 'd', 'e']
# print(f"The first three letters in the list are: {letters[:3]}")
# print(f"The three middle letters in the list are: {letters[1:4]}")
# print(f"The last three letters in the list are: {letters[-3:]}")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-11
# my_pizzas     = ['margherita', 'mozzarella', 'pepperoni']
# friend_pizzas = my_pizzas[:]

# my_pizzas.insert(0, 'double cheese')
# friend_pizzas.append('pineapple')

# print("My favorite pizzas are:")
# for pizza in my_pizzas:
#     print(pizza.title())

# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza.title())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-12
# for index in range(0, len(my_pizzas) - 1):
#     print(my_pizzas[index].title())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 4-13
# foods    = ('lasagna', 'pizza' 'spaghetti')
# foods[0] = 'roast beef' # This is supposed to generate a TypeError.
# foods    = ('roast beef', 'soup', 'spaghetti')
# print(foods)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *