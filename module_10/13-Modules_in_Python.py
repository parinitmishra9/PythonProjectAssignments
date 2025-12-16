# Modules in Python are files containing Python code that can define functions, classes, and variables.
# They allow for code organization and reuse across different programs.
# You can create your own modules or use built-in and third-party modules.
# To use a module, you typically import it using the import statement.
# Here are some examples of how to create and use modules in Python:
# Built-in Modules are pre-installed with Python and provide various functionalities.:
# Example 1: Using the math module to perform mathematical operations
import math
print("Square root of 16:", math.sqrt(16))  # Output: Square root of 16: 4.0
print("Value of pi:", math.pi)                # Output: Value of pi: 3.141592653589793
# Example 2: Using the random module to generate random numbers
import random
print("Random integer between 1 and 10:", random.randint(1, 10))  # Output: Random integer between 1 and 10: (varies)
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))  # Output: Random choice from a list: (varies)
# Example 3: Using the datetime module to work with dates and times
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)  # Output: Current date and time: (varies)
print("Current year:", now.year)       # Output: Current year: (varies)

# Aliasing Modules allows you to give a module a different name when importing it.
# Example 4: Importing the numpy module with an alias
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("Numpy array:", array)  # Output: Numpy array: [1 2 3 4 5]
# Example 5: Importing the pandas module with an alias
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)
# Output: Pandas DataFrame:
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35