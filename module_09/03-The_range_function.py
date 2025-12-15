# The range() function
# The range() function is used to generate a sequence of numbers.
# It can take one, two, or three arguments: start, stop, and step.
# The start argument is the first number in the sequence (inclusive).
# The stop argument is the number that stops the sequence (exclusive).
# The step argument is the difference between each number in the sequence.
# If only one argument is provided, it is treated as the stop value, and the start value defaults to 0.
# Example 1: Using range() with one argument
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
# Example 2: Using range() with two arguments
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6
# Example 3: Using range() with three arguments
for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9
# Example 4: Using range() with a negative step
for i in range(10, 0, -2):
    print(i)
# Output: 10, 8, 6, 4, 2
# Example 5: Converting range to a list
numbers = list(range(5))
print(numbers)
# Output: [0, 1, 2, 3, 4]
# Example 6: Using range() in a list comprehension
squares = [x**2 for x in range(6)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25]
# Example 7: Using range() with a for loop to iterate over indices
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i])
# Output: apple, banana, cherry
# Example 8: Using range() to create a countdown
for i in range(5, 0, -1):
    print(i)
# Output: 5, 4, 3, 2, 1