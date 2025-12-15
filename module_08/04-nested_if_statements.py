# Nested if statements allow you to check multiple conditions in a hierarchical manner. This means that you can have an if statement inside another if statement. Here's an example:
age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You are also eligible to drink alcohol in the US.")
    else:
        print("You are not eligible to drink alcohol in the US.")
else:
    print("You are a minor.")
# In this example, the outer if statement checks if the age is 18 or older. If this condition is True, it prints "You are an adult." Then, inside this block, there is another if statement that checks if the age is 21 or older. Depending on this inner condition, it prints whether the person is eligible to drink alcohol in the US or not. If the outer condition is False, it prints "You are a minor."
# You can nest multiple levels of if statements as needed, but be cautious not to make the code too complex or difficult to read.
