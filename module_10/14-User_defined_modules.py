# User defined modules in Python allow you to organize your code into separate files and reuse them across different programs. This helps in maintaining a clean codebase and promotes code reusability.
# To create a user-defined module, you simply create a new Python file (with a .py extension) and define functions, classes, or variables in it. You can then import this module into other Python files using the import statement.
# Here's an example of how to create and use a user-defined module:

# arithmetic.py
import arithmetic as arith

result_add = arith.add(10, 5)
print(f"Addition: {result_add}")

result_subtract = arith.subtract(10, 5)
print(f"Subtraction: {result_subtract}")

result_multiply = arith.multiply(10, 5)
print(f"Multiplication: {result_multiply}")

result_divide = arith.divide(10, 5)
print(f"Division: {result_divide}")

result_average = arith.average(10, 5)
print(f"Average: {result_average}")

result_square = arith.square(10)
print(f"Square: {result_square}")

result_square_root = arith.square_root(25)
print(f"Square Root: {result_square_root}")

result_factorial = arith.factorial(5)
print(f"Factorial: {result_factorial}")

result_power = arith.power(2, 3)
print(f"Power: {result_power}")

result_modulus = arith.modulus(10, 3)
print(f"Modulus: {result_modulus}")

result_integer_division = arith.integer_division(10, 3)
print(f"Integer Division: {result_integer_division}")

# In this example, we created a user-defined module named arithmetic.py that contains various arithmetic functions.
# We then imported this module in another Python file and used its functions to perform different arithmetic operations.