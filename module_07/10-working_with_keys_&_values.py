# In dictionaries, keys and values are fundamental components. Keys are unique identifiers used to access values,
# which can be of any data type. This code demonstrates how to work with keys and values in a dictionary.
#  keys can be of various data types including strings, numbers, and tuples, while values can be of any data type including lists, sets,
#  and even other dictionaries.
# why touples can be used as keys in dictionaries but lists cannot?
# because touples are immutable whereas lists are mutable and can be changed after their creation.
# Keys of dictionaries must be immutable types to ensure their hash value remains constant.
#  Values, on the other hand, can be of any data type, including mutable types like lists and sets.
# Example:
# Creating a dictionary with various types of keys and values
my_dict = {
    "name": "Alice",               # string key with string value
    42: [1, 2, 3],                 # integer key with list value
    (1, 2): {"a": 1, "b": 2},     # tuple key with dictionary value
    3.14: {1, 2, 3}              # float key with set value
}
print("Dictionary:", my_dict)
# Accessing values using keys
print("Name:", my_dict["name"])          # Output: Alice
print("List:", my_dict[42])              # Output: [1, 2, 3]
print("Dictionary:", my_dict[(1, 2)])    # Output: {'a': 1, 'b': 2}
print("Set:", my_dict[3.14])            # Output: {1, 2, 3}
# Iterating over keys
print("Keys:")
for key in my_dict.keys():
    print(key)
# Iterating over values
print("Values:")
for value in my_dict.values():
    print(value)
# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Checking if a key exists
key_to_check = "name"
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists with value: {my_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' does not exist.")
# Adding a new key-value pair
my_dict["age"] = 30
print("Updated Dictionary:", my_dict)
# Removing a key-value pair
removed_value = my_dict.pop(42)
print("Removed Value:", removed_value)
print("Dictionary after removal:", my_dict)

# fetch all keys from the dictionary and store them in a list
keys_list = list(my_dict.keys())
print("Keys List:", keys_list)
# fetch all values from the dictionary and store them in a list
values_list = list(my_dict.values())
print("Values List:", values_list)
# fetch all key-value pairs from the dictionary and store them in a list of tuples
items_list = list(my_dict.items())
print("Items List:", items_list)
# Output:
# Dictionary: {'name': 'Alice', 42: [1, 2, 3], (1, 2): {'a': 1, 'b': 2}, 3.14: {1, 2, 3}}
# Name: Alice
# List: [1, 2, 3]
# Dictionary: {'a': 1, 'b': 2}
# Set: {1, 2, 3}
# Keys:
# name
# 42
# (1, 2)
# 3.14
# Values:
# Alice
# [1, 2, 3]
# {'a': 1, 'b': 2}
# {1, 2, 3}
# Key-Value Pairs:
# name: Alice
# 42: [1, 2, 3]
# (1, 2): {'a': 1, 'b': 2}
# 3.14: {1, 2, 3}
# Key 'name' exists with value: Alice
# Updated Dictionary: {'name': 'Alice', 42: [1, 2, 3], (1, 2): {'a': 1, 'b': 2}, 3.14: {1, 2, 3}, 'age': 30}
# Removed Value: [1, 2, 3]
# Dictionary after removal: {'name': 'Alice', (1, 2): {'a: 1, 'b': 2}, 3.14: {1, 2, 3}, 'age': 30}
# Keys List: ['name', (1, 2), 3.14, 'age']
# Values List: ['Alice', {'a': 1, 'b': 2}, {1, 2, 3}, 30]
# Items List: [('name', 'Alice'), ((1, 2), {'a': 1, 'b': 2}), (3.14, {1, 2, 3}), ('age', 30)]