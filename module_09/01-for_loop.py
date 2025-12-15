# For loop in Python
# for loop is used to iterate over a sequence (like list, tuple, string) or other iterable objects (like sets, dictionaries)
# It allows you to execute a block of code repeatedly for each item in the sequence
# Syntax:
# for item in sequence:
#     # code block to be executed for each item
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Example 2: Iterating over a string
for char in "Hello":
    print(char)
# Example 3: Iterating over a set
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
# Example 4: Using range() to iterate over a sequence of numbers
for i in range(5):
    print(i)
# Example 5: Using for loop with else
for i in range(3):
    print(i)
else:
    print("Loop completed")
# Example 6: Nested for loop
for i in range(2):
    for j in range(2):
        print(f"i: {i}, j: {j}")