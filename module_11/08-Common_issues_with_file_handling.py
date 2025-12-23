# Common issues with file handling in Python
# 1. File Not Found Error
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")

# 2. Permission Denied Error
try:
    with open('/root/secret_file.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("Error: You do not have permission to access this file.")

# 3. File Already Exists Error
import os
file_path = 'existing_file.txt'
# Create the file first
with open(file_path, 'w') as file:
    file.write("This file already exists.")
try:
    with open(file_path, 'x') as file:
        file.write("Trying to create a file that already exists.")
except FileExistsError:
    print("Error: The file already exists.")
# Clean up
os.remove(file_path)
# 4. IOError (Input/Output Error)
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
# 8. Incorrect file mode
try:
    with open('some_file.txt', 'r') as file:
        file.write("Trying to write in read mode.")
except io.UnsupportedOperation:
    print("Error: Unsupported operation for the file mode.")
# Clean up
os.remove('some_file.txt')
# 9. File path issues
try:
    with open('invalid:/path/file.txt', 'r') as file:
        content = file.read()
except OSError:
    print("Error: Invalid file path.")
# 10. Disk full error (simulated)
try:
    with open('large_file.txt', 'wb') as file:
        file.write(b'0' * (10**10))  # Attempt to write a large file
except OSError:
    print("Error: Disk is full or quota exceeded.")
# Clean up
if os.path.exists('large_file.txt'):
    os.remove('large_file.txt')
# Note: Some errors like Disk full error may not be easily reproducible depending on the system state.
# 11. Handling exceptions with context managers
try:
    with open('another_non_existent_file.txt', 'r') as file:
        content = file.read()
except Exception as e:
    print(f"An error occurred: {e}")
# This demonstrates proper exception handling while using context managers.
# Clean up
if os.path.exists('another_non_existent_file.txt'):
    os.remove('another_non_existent_file.txt')
# End of common issues with file handling in Python