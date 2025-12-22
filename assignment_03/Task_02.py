## 📐 Task 2: Using the Math Module for Calculations

import math

def calculate_math_properties(number):
    if number <= 0:
        return "Number must be positive for logarithm and square root calculations."

    square_root = math.sqrt(number)
    logarithm = math.log(number)
    sine = math.sin(number)

    return square_root, logarithm, sine

try:
    user_input = float(input("Enter a positive number: "))
    results = calculate_math_properties(user_input)

    if isinstance(results, str):
        print(results)
    else:
        square_root, logarithm, sine = results
        print(f"Square root: {square_root}")
        print(f"Logarithm: {logarithm}")
        print(f"Sine: {sine}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
