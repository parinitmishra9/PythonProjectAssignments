# Types of arguments in Python functions
def example_function(pos_arg1, pos_arg2, default_arg1=10, default_arg2=20, *args, **kwargs):
    print("Positional Argument 1:", pos_arg1)
    print("Positional Argument 2:", pos_arg2)
    print("Default Argument 1:", default_arg1)
    print("Default Argument 2:", default_arg2)

    print("Additional Positional Arguments (args):", args)

    print("Keyword Arguments (kwargs):", kwargs)
# Calling the function with different types of arguments
example_function(1, 2)
print("-----")
example_function(1, 2, 30)
print("-----")
example_function(1, 2, 30, 40)
print("-----")
example_function(1, 2, 30, 40, 50, 60)
print("-----")
example_function(1, 2, 30, 40, 50, 60, key1='value1', key2='value2')

# Positional Argument - Arguments that are passed to a function based on their position.
# Example:
def add(a, b):
    print(f"a: {a}, b: {b}")
    return a + b
print(add(5, 10))
# Here, 5 is assigned to parameter 'a' and 10 to parameter 'b'.

# Default Argument - Arguments that have a default value if no value is provided during the function call.
# Example:
def add(a, b=10):
    print(f"a: {a}, b: {b}")
    return a + b
print(add(5, 15))
# Here, b takes the value 15 instead of the default value 10.
print(add(5))
# Here, b takes the default value 10.
# Note: Default arguments must come after positional arguments in the function definition.

# Keyword Argument - Arguments that are passed to a function by explicitly specifying the parameter name.
# Example:
def add(a, b=10, c=20):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c
print(add(10, c=30))
# Here, a takes the value 10, b takes the default value 10, and c takes the value 30.
