# Check if a file exists
# 1. using the os.path module
import os

file_path = 'example_with.txt'
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
# In this example, we use the os.path.exists() function to check if the specified file exists in the file system.
# The function returns True if the file exists and False otherwise.

# 2. using the pathlib module
from pathlib import Path
file_path = Path('example_with.txt')
if file_path.is_file():
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
# In this example, we use the is_file() method of the Path object to check if the specified file exists.
# The method returns True if the file exists and is a regular file, and False otherwise.
# Both methods are effective for checking file existence, and you can choose the one that best fits your coding style or project requirements.

#  3. using try-except block
file_path = 'example_with.txt'
try:
    with open(file_path, 'r') as file:
        print(f"The file '{file_path}' exists.")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
# In this example, we attempt to open the specified file in read mode.
# If the file exists, it will be opened successfully, and we print a message indicating its existence.
# If the file does not exist, a FileNotFoundError exception is raised, and we catch it to print a message indicating that the file does not exist.
# This method is useful when you want to perform an operation on the file if it exists, while also handling the case where it does not exist.

