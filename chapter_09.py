# Python Crash Course by Eric Matthes
# Chapter 09: Classes

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-1
# class Restaurant:
#     """
#     A simple attempt to model a restaurant.
#     """

#     def __init__(self, name, cuisine):
#         """
#         Initialize name and cuisine type attributes.
#         """
#         self.name = name
#         self.cuisine_type = cuisine


#     def describe_restaurant(self):
#         """
#         Print the restaurant attributes.
#         """
#         print(f"Restaurant name: {self.name.title()}")
#         print(f"Cuisine type: {self.cuisine_type}")


#     def open_restaurant(self):
#         """
#         Print a message telling the restaurant is open.
#         """
#         print(f"{self.name.title()} is now open.")


# my_restaurant = Restaurant("china in box", "chinese")
# print(my_restaurant.name)
# print(my_restaurant.cuisine_type)

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-2
# restaurant_1 = Restaurant("mister pizza", "pizzeria")
# restaurant_2 = Restaurant("bonaparte", "italian")
# restaurant_3 = Restaurant("spettus", "barbecue")

# restaurant_1.describe_restaurant()
# print("\n")

# restaurant_2.describe_restaurant()
# print("\n")

# restaurant_3.describe_restaurant()
# print("\n")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-3
# class User:

#     def __init__(self, first, last, gender, age, login_id):
#         """
#         Initialize the user attributes.
#         """
#         self.first_name = first
#         self.last_name = last
#         self.gender = gender
#         self.age = age
#         self.id = login_id


#     def describe_user(self):
#         """
#         Prints a summary of the user information.
#         """
#         print(f"\nBrief summary of {self.id} information:")
#         print(f"- Name: {self.first_name.title()} {self.last_name.title()}")
#         print(f"- Gender: {self.gender}")
#         print(f"- Age: {self.age}")


#     def greet_user(self):
#         """
#         Greets the user after a successful login.
#         """
#         print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


# user_1 = User('carlos', 'reis', 'M', 34, 'casreis')
# user_2 = User('thereza', 'souza', 'F', 63, 'tcarmen')

# user_1.describe_user()
# user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-4
# class Restaurant:
#     """
#     A simple attempt to model a restaurant.
#     """

#     def __init__(self, name, cuisine):
#         """
#         Initialize name and cuisine type attributes.
#         """
#         self.name = name
#         self.cuisine_type = cuisine
#         self.number_served = 0


#     def describe_restaurant(self):
#         """
#         Print the restaurant attributes.
#         """
#         print(f"Restaurant name: {self.name.title()}")
#         print(f"Cuisine type: {self.cuisine_type}")


#     def open_restaurant(self):
#         """
#         Print a message telling the restaurant is open.
#         """
#         print(f"{self.name.title()} is now open.")


#     def set_number_served(self, number):
#         """
#         Sets the number_served attribute to the number given as an argument.
#         """
#         self.number_served = number


#     def increment_number_served(self, increment_value):
#         """
#         Increment the number_served parameter by increment_value.
#         """
#         self.number_served += increment_value


# restaurant = Restaurant("pizza hut", "pizzeria")
# print(restaurant.number_served)

# restaurant.number_served = 200
# print(restaurant.number_served)

# restaurant.set_number_served(300)
# print(restaurant.number_served)

# restaurant.increment_number_served(1000)
# print(restaurant.number_served)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-5
# class User:

#     def __init__(self, first, last, gender, age, login_id):
#         """
#         Initialize the user attributes.
#         """
#         self.first_name = first
#         self.last_name = last
#         self.gender = gender
#         self.age = age
#         self.id = login_id
#         self.login_attempts = 0


#     def describe_user(self):
#         """
#         Prints a summary of the user information.
#         """
#         print(f"\nBrief summary of {self.id} information:")
#         print(f"- Name: {self.first_name.title()} {self.last_name.title()}")
#         print(f"- Gender: {self.gender}")
#         print(f"- Age: {self.age}")


#     def greet_user(self):
#         """
#         Greets the user after a successful login.
#         """
#         print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


#     def increment_login_attempts(self):
#         """
#         Increment login attempts by 1.
#         """
#         self.login_attempts += 1


#     def reset_login_attempts(self):
#         """
#         Sets login_attempts to 0.
#         """
#         self.login_attempts = 0


# user = User('carlos', 'reis', 'M', 34, 'casreis')
# print(user.login_attempts)

# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)

# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)

# user.reset_login_attempts()
# print(user.login_attempts)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-6
# class IceCreamStand(Restaurant):
#     """
#     Models an ice cream stand as a subclass of the Restaurant parent class.
#     """
#     def __init__(self, name, cuisine):
#         """
#         Initialize attributes of the Restaurant parent class.
#         Then initialize attributes specific to the IceCreamStand subclass.
#         """
#         super().__init__(name, cuisine)
#         self.flavors = ['chocolate', 'coconut', 'peanut', 'strawberry']


#     def display_flavors(self):
#         """
#         Display a list of available ice cream flavors.
#         """
#         print(f"The following flavors are available:")

#         for flavor in self.flavors:
#             print(f"- {flavor.title()}")


# my_stand = IceCreamStand("fri-sabor", "sorveteria")
# my_stand.open_restaurant()
# my_stand.display_flavors()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-7
# class Admin(User):
#     """
#     Models an admin as a subclass of the User parent class.
#     """
#     def __init__(self, first, last, gender, age, login_id):
#         """
#         Initialize attributes of the User parent class.
#         Then initialize attributes specific to the Admin subclass.
#         """
#         super().__init__(first, last, gender, age, login_id)
#         self.privileges = ["can add post", "can delete post", "can ban user"]


#     def show_privileges(self):
#         """
#         Show all the administrator privileges.
#         """
#         print(f"{self.id} has the following privileges:")

#         for privilege in self.privileges:
#             print(f"- {privilege.title()}")


# adm = Admin('carlos', 'reis', 'M', 34, 'casreis')
# adm.greet_user()
# adm.show_privileges()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-8
# class Privileges:
#     """
#     An attempt to model admin privileges.
#     """
#     def __init__(self):
#         """
#         Initialize the Privileges class attributes.
#         """
#         self.privileges = ["can add post", "can delete post", "can ban user"]


#     def show_privileges(self):
#         """
#         Shows a list of privileges.
#         """
#         print("You have the following privileges:")

#         for privilege in self.privileges:
#             print(f"- {privilege.title()}")


# class Admin(User):
#     """
#     Models an admin as a subclass of the User parent class.
#     """
#     def __init__(self, first, last, gender, age, login_id):
#         """
#         Initialize attributes of the User parent class.
#         Initialize privileges attribute with an instance of Privileges class.
#         """
#         super().__init__(first, last, gender, age, login_id)
#         self.privileges = Privileges()


# adm = Admin('carlos', 'reis', 'M', 34, 'casreis')
# adm.greet_user()
# adm.privileges.show_privileges()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-9
# class Car:
#     """
#     A simple attempt to represent a car.
#     """

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0


#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name


#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")


#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             sllf.odometer_reading = mileage
#         else:
#             print(f"You can't roll back the odometer!")


#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# class Battery:
#     """
#     Models a battery for an electric car.
#     """

#     def __init__(self, battery_size=75, battery_range=260):
#         self.size = battery_size
#         self.range = battery_range


#     def describe_battery(self):
#         print(f"This car has a {self.size}-kWh battery.")


#     def get_range(self):
#         """
#         Print a statement about the range this battery provides.
#         """
#         if self.size == 75:
#             self.range = 260
#         elif self.size == 100:
#             self.range = 315

#         print(f"This car can go about {self.range} miles on a full charge.")


#     def upgrade_battery(self):
#         if self.size < 100:
#             self.size = 100


# class ElectricCar(Car):
#     """
#     Represents aspects specific to electric cars.
#     """

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()


# my_car = ElectricCar('volkswagen', 'crossfox', '2014')
# my_car.battery.get_range()
# my_car.battery.upgrade_battery()
# my_car.battery.get_range()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-10
# from my_module import Restaurant

# restaurant = Restaurant("pizza hut", "pizzeria")
# print(restaurant.number_served)

# restaurant.number_served = 200
# print(restaurant.number_served)

# restaurant.set_number_served(300)
# print(restaurant.number_served)

# restaurant.increment_number_served(1000)
# print(restaurant.number_served)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-11
# from my_module import User, Privileges, Admin

# adm = Admin('carlos', 'reis', 'M', 34, 'casreis')
# adm.greet_user()
# adm.privileges.show_privileges()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-13
# from random import randint

# class Die:
#     """
#     Models a die with a set number of sides.
#     """
#     def __init__(self, sides=6):
#         self.sides = sides


#     def roll_die(self):
#         """
#         Simulates the action of rolling the die.
#         Prints a random integer between 1 and the number of sides of the die.
#         """
#         print(f"{randint(1, self.sides)}")


# my_die = Die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 9-15
# from random import choice

# lottery_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

# winner_ticket = []
# winner_ticket.append(choice(lottery_numbers))
# winner_ticket.append(choice(lottery_numbers))
# winner_ticket.append(choice(lottery_numbers))
# winner_ticket.append(choice(lottery_numbers))

# my_ticket = [0, 0, 0, 0]
# trial_counter = 1

# while my_ticket != winner_ticket:
#     my_ticket[0] = choice(lottery_numbers)
#     my_ticket[1] = choice(lottery_numbers)
#     my_ticket[2] = choice(lottery_numbers)
#     my_ticket[3] = choice(lottery_numbers)

#     trial_counter += 1

# print(f"The winner ticket is {winner_ticket}.")
# print(f"It took you {trial_counter} tries to win the lottery!")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *