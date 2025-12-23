# Reading files:
# In Python, you can read files using the built-in open() function. Here's a simple example of how to read a text file:
# Open a file in read mode
file = open('example.txt', 'r')
# Read the contents of the file
content = file.read()
# Print the contents
print(content)
# Close the file
file.close()

# If you want to read a file line by line, you can use a for loop:
# Open a file in read mode
file = open('example.txt', 'r')
# Read the file line by line
for line in file:
    print(line.strip())  # strip() removes leading/trailing whitespace
# Close the file
file.close()

# Alternatively, you can use the with statement to automatically handle closing the file:
# Open a file in read mode using with statement
with open('example.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Print the contents
    print(content)
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
# Reading a file line by line using with statement
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace
# This is the preferred way to work with files in Python as it is more concise and handles file closing automatically.

# You can also read specific number of characters or lines using read(size) or readline() methods:
# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read first 10 characters
    first_10_chars = file.read(10)
    print(first_10_chars)
    # Read the next line
    next_line = file.readline()
    print(next_line.strip())
# This code demonstrates how to read files in Python using different methods.

# readLine() reads a single line from the file, while read(size) reads a specified number of characters.
# Example of using readline():
# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read the first line
    first_line = file.readline()
    print(first_line.strip())
    # Read the second line
    second_line = file.readline()
    print(second_line.strip())
# Note:
# Each call to readline() reads the next line in the file.
# if you call readline() multiple times, it will continue from where it left off.
# and if there are no more lines to read, it will return an empty string.


# You can also use readlines() to read all lines into a list:
# Example of using readlines():
# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    # Print each line
    for line in lines:
        print(line.strip())
# This will read all lines from the file and store them in a list called lines, which you can then iterate over.
