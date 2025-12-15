# For loops with strings and dictionaries
# A for loop can iterate over the characters in a string
# or the key-value pairs in a dictionary.
# Example 1: Iterating over characters in a string
my_string = "Hello"
for char in my_string:
    print(char)
# Example 2: Iterating over key-value pairs in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# Example 3: Counting vowels in a string
vowel_count = 0
for char in my_string:
    if char.lower() in 'aeiou':
        vowel_count += 1
print(f"Number of vowels in '{my_string}': {vowel_count}")
# Example 4: Creating a new dictionary with squared values
squared_dict = {}
for key, value in my_dict.items():
    squared_dict[key] = value ** 2
print("Original dictionary:", my_dict)
print("Squared dictionary:", squared_dict)
# Example 5: Concatenating characters from a string
concatenated_string = ""
for char in my_string:
    concatenated_string += char + "-"
print("Concatenated string:", concatenated_string[:-1])  # Remove the last hyphen