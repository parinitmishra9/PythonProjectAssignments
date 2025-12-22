# User defined modules in Python allow you to organize your code into separate files and reuse them across different programs. This helps in maintaining a clean codebase and promotes code reusability.
# To create a user-defined module, you simply create a new Python file (with a .py extension) and define functions, classes, or variables in it. You can then import this module into other Python files using the import statement.
# Here's an example of how to create and use a user-defined module:
# arithmetic.py

"""
A simple arithmetic module.
"""

def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Return the difference of num1 and num2."""
    return num1 - num2

def multiply(num1, num2):
    """Return the product of num1 and num2."""
    return num1 * num2

def divide(num1, num2):
    """Return the division of num1 by num2."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def average(num1, num2):
    """Return the average of num1 and num2."""
    return (num1 + num2) / 2

def square(num):
    """Return the square of num."""
    return num ** 2

def square_root(num):
    """Return the square root of num."""
    return num ** 0.5

def factorial(num):
    """Return the factorial of num."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def modulus(num1, num2):
    """Return the modulus of num1 and num2."""
    return num1 % num2

def integer_division(num1, num2):
    """Return the integer division of num1 by num2."""
    return num1 // num2

