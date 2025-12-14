# List inside a list
l1 = [5, 1.5, "Python", True, None, [1,2,3], 10]
print(len(l1))
print(l1[-2])
print(len(l1[-2]))

print("-----------------------")
print()

# chain Indexing
print(l1[-2][1])

print("-----------------------")
print()

# List inside a list
l2 = [[1,2], [3,4], [5,6, [0, 1]]]
print(len(l2))
print(l2[2][-1][1])
print(l2[2][-1][-1])

print("-----------------------")
print()
