# Infinite while loop example
# while True:
#     print("This loop will run forever unless interrupted.")
# Note: To stop an infinite loop, you can use Ctrl+C in the terminal or interrupt the kernel in Jupyter notebooks.
# Caution: Be careful when running infinite loops as they can cause your program to hang.

correct_password = "Python"
while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
# This code will keep asking the user to enter the correct password until they do so.
