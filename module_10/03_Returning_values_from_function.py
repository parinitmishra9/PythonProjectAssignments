# Returning values from function using return statement
# The return statement is used to exit a function and return a value to the caller.
# When a return statement is executed, the function terminates, and the specified value is sent back to the caller.
# Defining a function that returns a value
def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    return a + b
# Calling the function and storing the returned value
result = add_numbers(5, 3)
print(f"The sum is: {result}")
# Output: The sum is: 8
# Function to check if a number is even or odd and return the result
def check_even_odd(number):
    """This function checks if a number is even or odd and returns the result."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Testing the function and storing the returned value
result = check_even_odd(10)
print(f"The number is: {result}")  # Output: The number is: Even
result = check_even_odd(7)
print(f"The number is: {result}")   # Output: The number is: Odd
# Function to calculate the factorial of a number and return the result
def factorial(n):
    """This function calculates the factorial of a number and returns the result."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Testing the factorial function
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")  # Output: The factorial of 5 is: 120
num = 0
result = factorial(num)
print(f"The factorial of {num} is: {result}")  # Output: The factorial of 0 is: 1
num = 1
result = factorial(num)
print(f"The factorial of {num} is: {result}")  # Output: The factorial of 1 is: 1

#  Note:
# In Python, if a function does not have a return statement, it returns None by default.
def no_return_function():
    """This function does not return any value."""
    print("This function does not return anything.")
# Calling the function
result = no_return_function()
print(f"The returned value is: {result}")  # Output: The returned value is: None
# You can also return multiple values from a function using tuples
def get_coordinates():
    """This function returns the x and y coordinates."""
    x = 10
    y = 20
    return x, y
# Calling the function and unpacking the returned values
x_coord, y_coord = get_coordinates()
print(f"X: {x_coord}, Y: {y_coord}")  # Output: X: 10, Y: 20
# Summary:
# The return statement is used to exit a function and return a value to the caller.
# Functions can return single or multiple values.
# If a function does not have a return statement, it returns None by default.