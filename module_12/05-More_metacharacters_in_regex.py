# More metacharacters in regex - \d, \D, \s, \S, \w, \W
import re

text = "The rain in Spain stays mainly in the plain 1234."
# Pattern to find all digits
pattern = r'\d+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for digits (\\d+):", matches)

# Pattern to find all non-digits
pattern = r'\D+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for non-digits (\\D+):", matches)

# Pattern to find all whitespace characters
pattern = r'\s+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for whitespace characters (\\s+):", matches)

# Pattern to find all non-whitespace characters
pattern = r'\S+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for non-whitespace characters (\\S+):", matches)

# Pattern to find all word characters
pattern = r'\w+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for word characters (\\w+):", matches)

# Pattern to find all non-word characters
pattern = r'\W+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for non-word characters (\\W+):", matches)

# Pattern to find words followed by digits
pattern = r'\w+\d+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for words followed by digits (\\w+\\d+):", matches)

#  ^ caret -> Start of string
pattern = r'^The'
matches = re.findall(pattern, text)
print("Matches for start of string (^The):", matches)

# $ dollar -> End of string
pattern = r'1234\.$'
matches = re.findall(pattern, text)
print("Matches for end of string (1234$):", matches)

# \b word boundary -> Word boundary is found at the position between a word character and a non-word character
pattern = r'\bain\b'
matches = re.findall(pattern, text)
print("Matches for word boundary (\\bain\\b):", matches)

#  () parentheses -> Grouping -> is used to group parts of a regex pattern together
pattern = r'(ain)'
matches = re.findall(pattern, text)
print("Matches for grouping ((ain)):", matches)

# () + | alternation -> is used to specify multiple alternatives in a regex pattern
pattern = r'rain|Spain|plain'
matches = re.findall(pattern, text)
print("Matches for alternation (rain|Spain|plain):", matches)