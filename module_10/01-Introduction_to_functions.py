# Introduction to functions in Python
# A function is a reusable block of code that performs a specific task.
# Functions help to organize code, improve readability, and reduce redundancy.
#  Built-in functions are pre-defined functions provided by Python, such as print(), len(), and type().
#  User-defined functions are functions created by the user to perform specific tasks.
# Defining a function
def greet(name):
    """This function greets the person passed as a parameter."""
    print(f"Hello, {name}!")
# Calling a function
greet("Alice")
greet("Bob")

# Function for checking even or odd numbers
def check_even_odd(number):
    """This function checks if a number is even or odd."""
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
# Testing the function
check_even_odd(10)  # Output: Even
check_even_odd(7)   # Output: Odd
