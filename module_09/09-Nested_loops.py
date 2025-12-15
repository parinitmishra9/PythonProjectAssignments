# Nested loops are loops inside other loops. They are useful for iterating over multi-dimensional data structures, such as lists of lists.
# Example 1: Iterating over a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row
# Example 2: Generating combinations of two lists
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']
for color in colors:
    for size in sizes:
        print(f"{color} - {size}")
# Example 3: Creating a multiplication table
print("Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=' ')
    print()  # New line after each row
# Example 4: Nested loops with conditionals
print("Even numbers in a 2D list:")
for row in matrix:
    for element in row:
        if element % 2 == 0:
            print(element, end=' ')
    print()  # New line after each row
# Example 5: Iterating over a list of dictionaries
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()  # New line after each person
# Example 6: Nested loops to create a pattern
print("Star Pattern:")
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()  # New line after each row
# These examples demonstrate how nested loops can be used to handle multi-dimensional data, generate combinations, create patterns, and work with complex data structures in Python.# Example 7: Iterating over a 3D list
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]
for layer in cube:
    for row in layer:
        for element in row:
            print(element, end=' ')
        print()  # New line after each row
    print()  # New line after each layer
# Example 8: Nested loops with list comprehension
squared_matrix = [[element ** 2 for element in row] for row in matrix]
print("Squared Matrix:")
for row in squared_matrix:
    print(row)
# Example 9: Nested loops to find common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common_elements.append(item1)
print(f"Common Elements: {common_elements}")
# Example 10: Nested loops to create a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
result_dict = {}
for i in range(len(keys)):
    result_dict[keys[i]] = values[i]
print(f"Resulting Dictionary: {result_dict}")