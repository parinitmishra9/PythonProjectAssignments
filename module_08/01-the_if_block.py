# Conditional Statements: The if Block
age = 20
if age >= 18:
    print("You are an adult.")

# The condition inside the if statement evaluates to True, so the indented block of code is executed, and "You are an adult." is printed to the console.
# If the condition were False, the code inside the if block would be skipped.
# ==, !=, >, <, >=, <= are some of the comparison operators used to form conditions in if statements.
# Example with a different condition
temperature = 30
if temperature > 25:
    print("It's a hot day.")
# In this example, since the temperature is 30, which is greater than 25, the message "It's a hot day." will be printed.
# If the temperature were 20, the message would not be printed because the condition would evaluate to False.
# You can also use variables and expressions in the condition
score = 85
passing_score = 60
if score >= passing_score:
    print("You passed the exam.")
# Here, since the score (85) is greater than or equal to the passing score (60), the message "You passed the exam." will be printed.
# If the score were 50, the message would not be printed.