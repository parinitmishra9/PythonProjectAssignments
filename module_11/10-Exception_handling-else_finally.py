# Exception handling - else & finally
# The else block is executed if no exceptions are raised in the try block.
# The finally block is executed regardless of whether an exception was raised or not.
# Example of try-except-else-finally block
import os

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
else:
    print("The result is:", result)
finally:
    print("Execution completed.")
# The finally block is useful for cleaning up resources, such as closing files or network connections.
# It ensures that the cleanup code is executed no matter what.
# Example of using finally for resource cleanup
file = None
try:
    file = open('example.txt', 'w')
    file.write("Hello, World!")
except IOError:
    print("Error: An I/O error occurred.")
finally:
    if file:
        file.close()
        print("File closed.")
    print("Error: Permission denied.")
# Clean up
os.chmod('read_only_file.txt', 0o666)  # Set file back to writable
os.remove('read_only_file.txt')