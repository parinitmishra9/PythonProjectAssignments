# The ternary Operator in Python
# The ternary operator allows you to evaluate something based on a condition being true or false in a single line of code.
# Syntax:
# value_if_true if condition else value_if_false
a = 10
b = 20
# Example 1: Find the maximum of two numbers
max_value = a if a > b else b
print("Maximum value is:", max_value)
# Example 2: Check if a number is even or odd
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")
# Example 3: Assign a grade based on score
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Score: {score}, Grade: {grade}")
# Example 4: Check if a string is empty or not
text = ""
status = "Empty" if not text else "Not Empty"
print(f"The string is {status}.")