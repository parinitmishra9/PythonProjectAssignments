# The with statement Context management in Python
# The with statement is used to wrap the execution of a block of code within methods defined by a context manager.
# This is commonly used for resource management, such as file handling, where it ensures that resources are properly acquired and released.
# Example of using the with statement for file handling
with open('example_with.txt', 'w') as file:
    file.write('Hello, World!')
# In this example, the with statement automatically handles closing the file after the block of code is executed,
# even if an exception occurs within the block.
# Custom context manager using the contextlib module(is a standard library module, which provides utilities for working with context managers and the with statement)
from contextlib import contextmanager
@contextmanager
def custom_context_manager():
    print("Entering the context")
    try:
        yield # Control is transferred to the block inside the with statement
    finally:
        print("Exiting the context")
# Using the custom context manager
with custom_context_manager():
    print("Inside the context")
# Output:
# Entering the context
# Inside the context
# Exiting the context