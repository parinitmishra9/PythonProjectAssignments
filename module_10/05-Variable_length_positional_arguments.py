# Variable length positional arguments:
# are used when you want to pass a variable number of arguments to a function.
# In Python, this is done using the *args syntax(0 to n).
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
result = add_numbers(1, 2, 3, 4, 5)
print("Sum:", result)  # Output: Sum: 15
# You can also pass a list or tuple using the * operator to unpack the arguments.
numbers = [1, 2, 3]
result = add_numbers(*numbers)
print("Sum from list:", result)  # Output: Sum from list: 6
# You can mix variable length positional arguments with regular positional arguments.
def multiply_and_add(multiplier, *args):
    total = 0
    for num in args:
        total += num
    return total * multiplier
result = multiply_and_add(2, 1, 2, 3)
print("Result:", result)  # Output: Result: 12

# Note that *args is just a convention; you can use any valid variable name preceded by an asterisk (*).
def concatenate_strings(*strings):
    result = ""
    for s in strings:
        result += s + " "
    return result.strip()
result = concatenate_strings("Hello", "world!", "This", "is", "Python.")
print("Concatenated String:", result)  # Output: Concatenated String: Hello world! This is Python.

# Note that you can also have zero arguments.
result = add_numbers()
print("Sum with no arguments:", result)  # Output: Sum with no arguments: 0
result = concatenate_strings()
print("Concatenated String with no arguments:", result)  # Output: Concatenated String with no arguments:

