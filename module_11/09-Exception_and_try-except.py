# Exception and try-except:
# Compile-time Error => Syntax Error and Indentation Error
# Exception and try-except: are used to handle runtime errors in Python.
# They allow the program to continue executing even if an error occurs.
# Runtime Error => ZeroDivisionError, NameError, TypeError, ValueError, IndexError
# Example of try-except block
try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
