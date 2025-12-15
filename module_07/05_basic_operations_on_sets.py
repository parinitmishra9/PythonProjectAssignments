nums = {1, 3, 2, 0, -1}

# Membership operator - in, not in
print(0 in nums)
print(10 not in nums)


nums_1 = {1, 3, 2, 0, -1}
nums_2 = {3, 5}
# concatenation? -> not possible
# print(nums_1 + nums_2)  # -> TypeError: unsupported operand type(s) for +: 'set' and 'set'
# repeating sets? -> not possible
# print(nums_1* 2) # -> TypeError: unsupported operand type(s) for *: 'set' and 'int'

# Type casting is possible from other data types to set like tuple, list, string, etc. and vice versa but order is not preserved
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays = set(weekdays)

# sets are mutable, we can add or remove elements from it
fruits = {"apple", "banana", "chikoo"}
print(fruits)
# adding an element
fruits.add("orange")
print(fruits)
# removing an element
fruits.remove("banana")
print(fruits)
# fruits.remove("banana")  # -> KeyError: 'banana' (if the element to be removed is not present in the set)
fruits.discard("banana")  # -> no error if the element to be removed is not present in the set
print(fruits)
# removing and returning an arbitrary element
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits after pop:", fruits)
# clearing the set
fruits.clear()
print("Fruits after clear:", fruits)