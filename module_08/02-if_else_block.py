# If else Block
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# In this example, since the age is 16, which is less than 18, the condition in the if statement evaluates to False. Therefore, the code inside the else block is executed, and "You are a minor." is printed to the console.
# The else block provides an alternative set of instructions that are executed when the condition in the if statement is False.
# Example with temperature
temperature = 20
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not a hot day.")
# Here, since the temperature is 20, which is not greater than 25, the condition evaluates to False, and the message "It's not a hot day." is printed.
# Example with exam score
score = 50
passing_score = 60
if score >= passing_score:
    print("You passed the exam.")
else:
    print("You did not pass the exam.")
# In this case, since the score (50) is less than the passing score (60), the condition evaluates to False, and the message "You did not pass the exam." is printed.
# The else block is optional; you can have an if statement without an else block if you only want to execute code when the condition is True.
# However, using else allows you to handle both outcomes of the condition.