# Function as an argument in Python are functions that can take other functions as parameters.
# and also known as higher-order functions.
def greet(name):
    return f"Hello, {name}!"
def farewell(name):
    return f"Goodbye, {name}!"
def process_name(name, func):
    return func(name)
# Using the functions as arguments
print(process_name("Alice", greet))      # Output: Hello, Alice!
print(process_name("Bob", farewell))     # Output: Goodbye, Bob!
# You can also use lambda functions as arguments
print(process_name("Charlie", lambda name: f"Welcome, {name}!"))  # Output: Welcome, Charlie!

# Example with built-in higher-order function 'map'
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Example with built-in higher-order function 'filter'
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# Example with built-in higher-order function 'sorted'
unsorted_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(unsorted_numbers, key=lambda x: x)
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
# These examples demonstrate how functions can be passed as arguments to other functions in Python.