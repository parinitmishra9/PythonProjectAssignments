# if-elif-else Statements
# The if-elif-else statement allows you to check multiple conditions and execute different blocks of code based on which condition is True. It provides a way to handle more than two possible outcomes.
# Syntax:
# if condition1:
#     # code block to be executed if condition1 is True
# elif condition2:
#     # code block to be executed if condition2 is True
# else:
#     # code block to be executed if none of the above conditions are True
# Example:
age = 25
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
# In this example, the program checks the value of age against multiple conditions. Since age is 25, which is not less than 13 or 20, the code inside the else block is executed, and "You are an adult." is printed to the console.
# You can have multiple elif blocks to check for various conditions. The program will evaluate each condition in order, and the first condition that evaluates to True will have its corresponding code block executed. If none of the conditions are True, the code inside the else block will be executed.
# Example with temperature
temperature = 15
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
elif temperature > 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")
# Here, since the temperature is 15, the program checks each condition in order. The first two conditions are False, but the third condition (temperature > 10) is True, so "It's a cool day." is printed to the console.
# Example with exam score
score = 75
if score >= 90:
    print("You received an A grade.")
elif score >= 80:
    print("You received a B grade.")
elif score >= 70:
    print("You received a C grade.")
else:
    print("You need to improve your score.")
# In this case, since the score is 75, the program checks each condition in order. The first two conditions are False, but the third condition (score >= 70) is True, so "You received a C grade." is printed to the console.
# The if-elif-else structure allows for more complex decision-making in your code by enabling multiple conditions to be evaluated sequentially.