# Introduction to File handling in Python
# File handling is an essential part of programming that allows you to read from and write to files on your computer.
# In Python, file handling is done using built-in functions and methods.
# Here are some basic operations for file handling in Python:
# 1. Opening a file
# 2. Reading from a file
# 3. Writing to a file
# 4. Closing a file
# Let's go through each of these operations with examples.
# 1. Opening a file
# You can open a file using the built-in open() function. The open() function takes two arguments: the file name and the mode (read, write, append, etc.).
# Example:
file = open('example.txt', 'r')  # Open a file in read mode
# 2. Reading from a file
# You can read the contents of a file using methods like read(), readline(), or readlines().
# Example:
content = file.read()  # Read the entire file
print(content)
file.close()  # Close the file after reading
# 3. Writing to a file
# You can write to a file using the write() or writelines() methods. Make sure to open the file in write ('w') or append ('a') mode.
# Example:
file = open('example_write.txt', 'w')  # Open a file in write mode
file.write('Hello, World!\n')  # Write a string to the file
file.write('This is a file handling example in Python.\n')
file.close()  # Close the file after writing
# 4. Closing a file
# It is important to close a file after you are done with it to free up system resources.
# You can close a file using the close() method, as shown in the examples above.
# Alternatively, you can use the with statement to automatically close the file after the block of code is executed.
# Example:
with open('example_write.txt', 'r') as file:
    content = file.read()
    print(content)
# In this example, the file is automatically closed after the with block is executed.
# This is a basic introduction to file handling in Python. You can explore more advanced topics like file modes, error handling, and working with different file formats as you progress.
# End of the file handling introduction.