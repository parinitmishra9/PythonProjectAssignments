# Special characters in regex are characters that have a specific meaning and function within a regex pattern.
# They are used to define patterns for matching strings in a more flexible and powerful way.
# Here are some common special characters in regex:
# . (dot): Matches any single character except a newline.
# ^ (caret): Matches the start of a string.
# $ (dollar sign): Matches the end of a string.
# * (asterisk): Matches zero or more occurrences of the preceding element.
# + (plus): Matches one or more occurrences of the preceding element.
# ? (question mark): Matches zero or one occurrence of the preceding element.
# \ (backslash): Escapes a special character, allowing it to be treated as a literal character.
# | (pipe): Acts as a logical OR between two patterns.
# () (parentheses): Groups patterns together and captures the matched content.
# [] (square brackets): Defines a character class, matching any one of the characters inside the brackets.
# {} (curly braces): Specifies a quantifier for the preceding element, indicating how many times it should occur.
# Here are some examples of how these special characters can be used in regex patterns:

# Note: r before the string denotes a raw string, which treats backslashes as literal characters.
# examples: "old\new" -> r"old\new": if we don't use r before the string, Python will treat \n as a newline character.

import re

# Sample text
text = "The current Python version is 3.14. The previous versions were 3.13, 3.12, and 2.7."

# Example 1: Using dot (.) to match any character
pattern_dot = r'3.1.'
matches_dot = re.findall(pattern_dot, text)
print("Matches using dot (.) metacharacter:", matches_dot)
# Output: ['3.14', '3.13', '3.12']
# Example 2: Using caret (^) to match the start of the string
pattern_start = r'^The'
match_start = re.search(pattern_start, text)
print("Match using caret (^):", match_start.group() if match_start else "No match")
# Output: 'The'
# Example 3: Using dollar sign ($) to match the end of the string
pattern_end = r'2\.7\.$'
match_end = re.search(pattern_end, text)
print("Match using dollar sign ($):", match_end.group() if match_end else "No match")
# Output: '2.7.'
# Example 4: Using asterisk (*) to match zero or more occurrences
pattern_asterisk = r'3\.1\d*'
matches_asterisk = re.findall(pattern_asterisk, text)
print("Matches using asterisk (*):", matches_asterisk)
# Output: ['3.14', '3.13', '3.12']
# Example 5: Using plus (+) to match one or more occurrences
pattern_plus = r'3\.1\d+'
matches_plus = re.findall(pattern_plus, text)
print("Matches using plus (+):", matches_plus)
# Output: ['3.14', '3.13', '3.12']
# Example 6: Using question mark (?) to match zero or one occurrence
pattern_question = r'3\.1\d?'
matches_question = re.findall(pattern_question, text)
print("Matches using question mark (?):", matches_question)
# Output: ['3.1', '3.1', '3.1']
# Example 7: Using backslash (\) to escape special characters
pattern_escape = r'3\.14'
match_escape = re.search(pattern_escape, text)
print("Match using backslash (\\):", match_escape.group() if match_escape else "No match")
# Output: '3.14'
# Example 8: Using pipe (|) for logical OR
pattern_or = r'3\.14|2\.7'
matches_or = re.findall(pattern_or, text)
print("Matches using pipe (|):", matches_or)
# Output: ['3.14', '2.7']
# Example 9: Using parentheses () for grouping
pattern_group = r'(3\.1\d)'
matches_group = re.findall(pattern_group, text)
print("Matches using parentheses () for grouping:", matches_group)
# Output: ['3.14', '3.13', '3.12']
# Example 10: Using square brackets [] for character classes
pattern_class = r'[23]\.\d+'
matches_class = re.findall(pattern_class, text)
print("Matches using square brackets [] for character classes:", matches_class)
# Output: ['3.14', '3.13', '3.12', '2.7']
# Example 11: Using curly braces {} for quantifiers
pattern_quantifier = r'3\.1\d{2}'
matches_quantifier = re.findall(pattern_quantifier, text)
print("Matches using curly braces {} for quantifiers:", matches_quantifier)
# Output: ['3.14', '3.13', '3.12']


# These examples demonstrate how special characters in regex can be used to create powerful and flexible patterns for string matching.

# \d - matches any digit (equivalent to [0-9]).
# \D - matches any non-digit character (equivalent to [^0-9]).
# \w - matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
# \W - matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_]).
# \s - matches any whitespace character (spaces, tabs, newlines).
# \S - matches any non-whitespace character.
# Example 12: Using \d, \D, \w, \W, \s, \S
pattern_special = r'\d+|\D+|\w+|\W+|\s+|\S+'
matches_special = re.findall(pattern_special, text)
print("Matches using \\d, \\D, \\w, \\W, \\s, \\S:", matches_special)
# Output: ['3', '.', '14', '.', 'The', ' ', 'current', ' ', 'Python', ' ', 'version', ' ', 'is', ' ', '3', '.', '14', '.', 'The', ' ', 'previous', ' ', 'versions', ' ', 'were', ' ', '3', '.', '13', ',', ' ', '3', '.', '12', ',', ' ', 'and', ' ', '2', '.', '7', '.']
# These patterns match digits, non-digits, alphanumeric characters, non-alphanumeric characters, whitespace, and non-whitespace characters in the text.
# The output will show the matches found using various special characters in regex.