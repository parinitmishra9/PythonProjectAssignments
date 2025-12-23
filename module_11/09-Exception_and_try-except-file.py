# Exception and try-except for File Handling in Python
# This code demonstrates how to handle exceptions that may occur during file operations using try-except blocks.
import os
# 1. File not found error
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
# 2. Permission denied error
try:
    with open('/root/secret_file.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("Error: Permission denied.")
# 3. File already exists error
file_path = 'existing_file.txt'
# Create the file first
with open(file_path, 'w') as file:
    file.write("This file already exists.")
try:
    with open(file_path, 'x') as file:
        file.write("Trying to create a file that already exists.")
except FileExistsError:
    print("Error: File already exists.")
# Clean up
os.remove(file_path)
# 4. IOError (Input/Output error)
try:
    with open('/dev/full', 'w') as file:
        file.write("This will cause an IOError.")
except IOError:
    print("Error: An I/O error occurred.")
# 5. Using a closed file
try:
    file = open('some_file.txt', 'w')
    file.close()
    file.write("Trying to write to a closed file.")
except ValueError:
    print("Error: I/O operation on closed file.")
# Clean up
os.remove('some_file.txt')
# 6. Reading a binary file in text mode
try:
    with open('binary_file.bin', 'wb') as file:
        file.write(b'\x00\x01\x02\x03')
    with open('binary_file.bin', 'r') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Cannot read binary file in text mode.")
# Clean up
os.remove('binary_file.bin')
# 7. Writing to a read-only file
try:
    with open('read_only_file.txt', 'w') as file:
        file.write("This is a read-only file.")
    os.chmod('read_only_file.txt', 0o444)  # Set file to read-only
    with open('read_only_file.txt', 'w') as file:
        file.write("Trying to write to a read-only file.")
except PermissionError:
    print("Error: Cannot write to a read-only file.")
# Clean up
os.remove('read_only_file.txt')

# Note: Some of these errors may not occur on all operating systems or configurations.
# For example, IOError on '/dev/full' is specific to Unix-like systems.
# Also, ensure you have the necessary permissions to create and delete files in the working directory.