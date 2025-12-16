# Local and Global variables in Python
# Global variable is defined outside any function and can be accessed anywhere in the code.
# Local variable is defined inside a function and can only be accessed within that function.
# Here is an example to illustrate the difference between local and global variables:
# Global variable
x = 10
def my_function():
    # Local variable
    y = 5
    print("Inside the function:")
    print("x (global):", x)  # Accessing global variable
    print("y (local):", y)   # Accessing local variable
my_function()
print("Outside the function:")
print("x (global):", x)      # Accessing global variable
# print("y (local):", y)     # This will raise an error because y is not defined outside the function
# To modify a global variable inside a function, you can use the 'global' keyword:
def modify_global():
    global x  # Declare x as global to modify it
    x = 20
modify_global()
print("After modifying global variable:")
print("x (global):", x)      # Now x is modified to 20
# In summary, local variables are confined to the function they are defined in, while global variables can be accessed and modified from anywhere in the code using the 'global' keyword.
# Output:
# Inside the function:
# x (global): 10
# y (local): 5
# Outside the function:
# x (global): 10
# After modifying global variable:
# x (global): 20

# Note:
# **1. If the value of global variable is changed in side the function using 'global' keyword, the change will be reflected outside the function as well.
# 2. and if the global variable is not declared using 'global' keyword inside the function, a new local variable with the same name will be created instead of modifying the global variable.**
# 3. If global variable is not declared using 'global' keyword inside the function, a new local variable with the same name will be created instead of modifying the global variable.