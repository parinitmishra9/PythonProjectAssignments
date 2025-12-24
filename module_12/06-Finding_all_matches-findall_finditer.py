# Finding all matches - findall, finditer methods
import re

text = "The rain in Spain stays mainly in the plain."

# Using findall to get all matches of 'ain'
matches = re.findall(r'ain', text)
print("Using findall:")
print(matches)  # Output: ['ain', 'ain', 'ain', 'ain']

# Using finditer to get an iterator of match objects for 'ain'
print("\nUsing finditer:")
for match in re.finditer(r'ain', text):
    print(f"Match: {match.group()} at position {match.start()}-{match.end()}")
# Output:
# Match: ain at position 5-8
# Match: ain at position 14-17
# Match: ain at position 27-30
# Match: ain at position 39-42

# Using findall to get all words that start with 'S' or 's'
words_starting_with_s = re.findall(r'\b[Ss]\w*', text)
print("\nWords starting with 'S' or 's':")
print(words_starting_with_s)  # Output: ['Spain', 'stays']