"""
This module contains functions and classes used in the exercises.
"""

def get_formatted_city(city, country, population=0):
    """
    Returns a neatly formatted string about the city.
    """
    if population > 0:
        string = f"{city.title()}, {country.title()} - population {population}"
    else:
        string = f"{city.title()}, {country.title()}"
    return string


def get_formatted_name(first, last, middle=''):
    """
    Generates a neatly formatted full name.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
    

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


class Employee:
    """
    A simple attempt to model an employee.
    """
    def __init__(self, first_name, last_name, salary):
        """
        Initializes the employee attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def give_raise(self, raise_value=5000):
        """
        Gives the employee a raise in salary.
        A custom raise_value can be passed as argument.
        If no argument is provided, default raise is $5,000.
        """
        self.salary += raise_value


class AnonymousSurvey:
    """
    Collect anonymous answers to a survey question.
    """
    def __init__(self, question):
        """
        Stores a question and prepares to store responses.
        """
        self.question = question
        self.responses = []


    def show_question(self):
        """
        Shows the survey question.
        """
        print(self.question)


    def store_response(self, new_response):
        """
        Stores a single response to the survey.
        """
        self.responses.append(new_response)


    def show_results(self):
        """
        Show all the responses that have been given.
        """
        for response in self.responses:
            print(f"- {response}")


class Restaurant:
    """
    A simple attempt to model a restaurant.
    """

    def __init__(self, name, cuisine):
        """
        Initialize name and cuisine type attributes.
        """
        self.name = name
        self.cuisine_type = cuisine
        self.number_served = 0


    def describe_restaurant(self):
        """
        Print the restaurant attributes.
        """
        print(f"Restaurant name: {self.name.title()}")
        print(f"Cuisine type: {self.cuisine_type}")


    def open_restaurant(self):
        """
        Print a message telling the restaurant is open.
        """
        print(f"{self.name.title()} is now open.")


    def set_number_served(self, number):
        """
        Sets the number_served attribute to the number given as an argument.
        """
        self.number_served = number


    def increment_number_served(self, increment_value):
        """
        Increment the number_served parameter by increment_value.
        """
        self.number_served += increment_value


class User:

    def __init__(self, first, last, gender, age, login_id):
        """
        Initialize the user attributes.
        """
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age
        self.id = login_id
        self.login_attempts = 0


    def describe_user(self):
        """
        Prints a summary of the user information.
        """
        print(f"\nBrief summary of {self.id} information:")
        print(f"- Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"- Gender: {self.gender}")
        print(f"- Age: {self.age}")


    def greet_user(self):
        """
        Greets the user after a successful login.
        """
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


    def increment_login_attempts(self):
        """
        Increment login attempts by 1.
        """
        self.login_attempts += 1


    def reset_login_attempts(self):
        """
        Sets login_attempts to 0.
        """
        self.login_attempts = 0


class Privileges:
    """
    An attempt to model admin privileges.
    """
    def __init__(self):
        """
        Initialize the Privileges class attributes.
        """
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """
        Shows a list of privileges.
        """
        print("You have the following privileges:")

        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    """
    Models an admin as a subclass of the User parent class.
    """
    def __init__(self, first, last, gender, age, login_id):
        """
        Initialize attributes of the User parent class.
        Initialize privileges attribute with an instance of Privileges class.
        """
        super().__init__(first, last, gender, age, login_id)
        self.privileges = Privileges()