# Star pattern using for loops
print("Star Pattern:")
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()  # New line after each row
# These examples demonstrate how nested loops can be used to handle multi-dimensional data, generate combinations, create patterns, and work with complex data structures in Python.
# Example 7: Iterating over a 3D list
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