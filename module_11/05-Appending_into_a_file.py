# Appending into a file: Write a Python program to append text to an existing file. If the file does not exist, create it.
# Open the file in append mode ('a'). If the file does not exist, it will be created.
file_path = 'example_a.txt'
with open(file_path, 'a') as file:
    # Append text to the file
    file.write('This is an appended line.\n')
print(f'Text has been appended to {file_path}.')

# Verify the content of the file
with open(file_path, 'r') as file:
    content = file.read()
    print('Current content of the file:')
    print(content)
# Output:
# Text has been appended to example_a.txt.
# Current content of the file:
# This is an appended line.
# If you run the program multiple times, it will keep appending the line to the file.

