"""
extend()
remove()
pop()
"""

fruits = ["Mango", "Apple", "Orange"]
print(fruits)

# extend
fruits.extend(["Banana", "Pineapple", "Banana"])
print(fruits)


print("-----------------------")
print()

# remove
print(fruits)
fruits.remove("Banana")
print(fruits)

print("-----------------------")
print()

# pop
print(fruits)
# fruits.pop(4)
fruits.pop(-1)
print(fruits)

# if no argument -> last one will be deleted
fruits.pop()
print(fruits)


print("-----------------------")
print()
