# Frozen sets are immutable sets in Python. They cannot be changed after they are created.
# They are created using the frozenset() function.
# Creating a frozen set
frozen_set1 = frozenset([1, 2, 3, 4, 5])
print("Frozen Set 1:", frozen_set1)
print("Type of Frozen Set 1:", type(frozen_set1))

# Attempting to add an element to a frozen set (will raise an error)
try:
    frozen_set1.add(6)
except AttributeError as e:
    print("Error:", e)

# Attempting to remove an element from a frozen set (will raise an error)
try:
    frozen_set1.remove(3)
except AttributeError as e:
    print("Error:", e)

# Creating another frozen set
frozen_set2 = frozenset(["apple", "banana", "cherry"])
frozen_set3 = frozenset(["apple", "banana", "chiku"])
print("Frozen Set 2:", frozen_set2)
print("Type of Frozen Set 2:", type(frozen_set2))

# Intersection of two frozen sets
intersection = frozen_set2.intersection(frozen_set3)
print("Intersection of Frozen Set 2 and Frozen Set 3:", intersection)   # -> {'apple', 'banana'}
# Union of two frozen sets
union = frozen_set2.union(frozen_set3)
print("Union of Frozen Set 2 and Frozen Set 3:", union)  # -> {'banana', 'cherry', 'chiku', 'apple'}
# Difference of two frozen sets
difference = frozen_set2.difference(frozen_set3)
print("Difference of Frozen Set 2 and Frozen Set 3:", difference)  # -> {'cherry'}





# Demonstrating that frozen sets can be used as dictionary keys
frozen_dict = {frozen_set1: "Numbers", frozen_set2: "Fruits"}
print("Dictionary with Frozen Sets as keys:", frozen_dict)