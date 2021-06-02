# Python Crash Course by Eric Matthes
# Chapter 11: Testing your code

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 11-2
# import unittest
# from my_module import get_formatted_city

# class CityTestCase(unittest.TestCase):
#     """
#     A test case for the get_formatted_city function.
#     """
#     def test_city_country(self):
#         """
#         Does it work without the 'population' arg?
#         """
#         city = get_formatted_city('santiago', 'chile')
#         self.assertEqual(city, 'Santiago, Chile')


#     def test_city_country_population(self):
#         """
#         Does it work with the 'population' arg?
#         """
#         city = get_formatted_city('santiago', 'chile', 5_000_000)
#         self.assertEqual(city, 'Santiago, Chile - population 5000000')


# if __name__ == '__main__':
#     unittest.main()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Exercise 11-3
# import unittest
# from my_module import Employee

# class TestEmployee(unittest.TestCase):
#     """
#     Tests for the class Employee.
#     """
#     def setUp(self):
#         """
#         Creates an employee and a custom salary raise for further testing.
#         """
#         self.employee = Employee("Michael", "Jackson", 2500)
#         self.raise_value = 500


#     def test_default_raise(self):
#         """
#         Tests give_raise function using the deafult raise value.
#         """
#         self.employee.give_raise()
#         self.assertEqual(7500, self.employee.salary)


#     def test_custom_raise(self):
#         """
#         Tests give_raise function with a custom raise value.
#         """
#         self.employee.give_raise(self.raise_value)
#         self.assertEqual(3000, self.employee.salary)


# if __name__ == '__main__':
#     unittest.main()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *