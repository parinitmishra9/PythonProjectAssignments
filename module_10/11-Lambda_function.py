# Lambda function in Python are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have a single expression.
# Syntax: lambda arguments: expression
# Example 1: A simple lambda function that adds 10 to the input
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
# Example 2: A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
# Example 3: A lambda function used with the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Example 4: A lambda function used with the filter() function to filter even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# Example 5: A lambda function used with the sorted() function to sort a list of tuples based on the second element
tuples = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
# These examples demonstrate how lambda functions can be used in Python for simple operations and in combination with other functions.
