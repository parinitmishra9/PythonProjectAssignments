# What is __name__: Understanding the __name__ variable in Python
# In Python, __name__ is a special built-in variable that represents the name of the current module.
# When a Python file is run directly, the __name__ variable is set to "__main__".
# However, when the same file is imported as a module in another file, the __name__ variable is set to the name of the module.
# This behavior allows you to write code that can be executed both as a standalone script and as a module.
# By using the __name__ variable, you can control the execution of certain parts of your code based on how the file is being used.
# Here's an example to illustrate the concept:
# example_module.py
def greet():
    print("Hello from the example_module!")


if __name__ == "__main__":
    greet()
    print("This code is running directly.")
else:
    print("This code is running as a module.")
# In this example, if you run example_module.py directly, it will output:
# Hello from the example_module!
# This code is running directly.
# However, if you import example_module in another Python file, it will output:
# This code is running as a module.
# Understanding the __name__ variable is crucial for writing modular and reusable code in Python.