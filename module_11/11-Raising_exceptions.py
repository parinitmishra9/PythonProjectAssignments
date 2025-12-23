# Raising exceptions in Python
# Raising exceptions allows you to create custom error conditions in your code.
# You can use the raise statement to trigger an exception when a specific condition is met.
# This is useful for validating input, enforcing constraints, or signaling errors in your program's logic.
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
try:
    result = divide_numbers(10, 0)
    print("The result is:", result)
except ValueError as ve:
    print("Error:", ve)
# Custom exception class
class NegativeNumberError(Exception):
    pass
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
try:
    check_positive(-5)
except NegativeNumberError as nne:
    print("Error:", nne)
# Raising built-in exceptions
def access_list_element(lst, index):
    if index >= len(lst):
        raise IndexError("List index out of range.")
    return lst[index]
my_list = [1, 2, 3]
try:
    element = access_list_element(my_list, 5)
    print("Element:", element)
except IndexError as ie:
    print("Error:", ie)
# Raising exceptions for input validation
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 120:
        raise ValueError("Age seems unrealistic.")
    return True
try:
    validate_age(-10)
except ValueError as ve:
    print("Error:", ve)
try:
    validate_age(150)
except ValueError as ve:
    print("Error:", ve)
# Successful validation
try:
    if validate_age(25):
        print("Age is valid.")
except ValueError as ve:
    print("Error:", ve)

# Example of raising Generic Exception
def check_string_length(s):
    if len(s) < 5:
        raise Exception("String length must be at least 5 characters.")
    return True
try:
    check_string_length("abc")
except Exception as e:
    print("Error:", e)