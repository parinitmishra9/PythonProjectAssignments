# Dictionaries in Python
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
# Creating a dictionary
my_dict = {"Name": "Alice", "Age": 25, "City": "New York"}
print(my_dict)
print(type(my_dict))
# Accessing values using keys
print("Name:", my_dict["Name"])
print("Age:", my_dict["Age"])
# Adding a new key-value pair
my_dict["Profession"] = "Engineer"
print("Updated Dictionary:", my_dict)
# Modifying an existing value
my_dict["Age"] = 26
print("Modified Dictionary:", my_dict)
# Removing a key-value pair
del my_dict["City"]
print("Dictionary after deletion:", my_dict)
# Length of the dictionary
print("Length of Dictionary:", len(my_dict))
# Dictionary with mixed data types
mixed_dict = {1: "One", "Two": 2, 3.0: [1, 2, 3]}
print("Mixed Dictionary:", mixed_dict)
# Accessing value using a key
print("Value for key 'Two':", mixed_dict["Two"])
# Note: Dictionaries do not allow duplicate keys. If a duplicate key is used, the last value will overwrite the previous one.
dup_dict = {"a": 1, "b": 2, "a": 3}
print("Dictionary with duplicate keys:", dup_dict)  # Output will be {'a': 3, 'b': 2}

# Indexing and slicing are not applicable to dictionaries as they are key-value pairs.
# print(my_dict[0])  # This will raise an error
# However, you can access values using their keys.

# You can also use the get() method to access values
print("Using get() method:", my_dict.get("Name"))
# Iterating through a dictionary
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
# Checking if a key exists
if "Age" in my_dict:
    print("Age is present in the dictionary.")
# Clearing all items from the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)