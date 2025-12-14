# Slicing of lists
l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(len(l1))
print(l1[1:6:1])
print(l1[2:7:2])

print("-----------------------")
print()

# concatenation of lists
l1 = [1, 7, 2]
l2 = [0, 5]
print(l1 + l2)
print(l2 + l1)

print("-----------------------")
print()

# repetition of lists
print(l2 * 3)

print("-----------------------")
print()

# append()
# adds an item to the end of the list

fruits = ["Mango", "Apple", "Orange"]
print(fruits)
# Syntax: list.append(item)
fruits.append("Pineapple")
print(fruits)

print("-----------------------")
print()

# insert
# adds an element before the specified index
# syntax: list.insert(index, item)
fruits.insert(0, "Banana")
print(fruits)
fruits.insert(3, "Pomegranate")
print(fruits)

print("-----------------------")
print()


