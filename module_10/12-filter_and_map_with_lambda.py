# filter() and map() with lambda functions in Python are powerful tools for processing and transforming data in a concise manner.
# The filter() function is used to filter elements from an iterable based on a condition defined by a lambda function.
# The map() function is used to apply a transformation to each element in an iterable using a lambda function.
# Here are examples of how to use filter() and map() with lambda functions:
# Example 1: Using filter() with a lambda function to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: Even numbers: [2, 4, 6, 8, 10]
# Example 2: Using map() with a lambda function to square each number in a list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)  # Output: Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Example 3: Using filter() with a lambda function to get numbers greater than 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print("Numbers greater than 5:", greater_than_five)  # Output: Numbers greater than 5: [6, 7, 8, 9, 10]
# Example 4: Using map() with a lambda function to convert temperatures from Celsius to Fahrenheit
celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = list(map(lambda c: (c * 9/5) + 32, celsius_temperatures))
print("Fahrenheit temperatures:", fahrenheit_temperatures)  # Output: Fahrenheit temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]
# These examples demonstrate how filter() and map() can be effectively used with lambda functions to process and transform data in Python.

# Summary:
# - filter() with lambda: Filters elements from an iterable based on a condition.
# - map() with lambda: Transforms each element in an iterable using a specified function.