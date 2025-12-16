# Docstrings in Python functions
# are used to describe the purpose and behavior of a function.
# They are enclosed in triple quotes and are placed immediately
# after the function definition.
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

# Help function to display the docstring
help(add)
# Example usage of the add function
result = add(5, 3)
print("The sum is:", result)