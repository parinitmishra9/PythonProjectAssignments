# The dot metacharacter and character classes in RegEx
import re

# Sample text
text = "The current Python version is 3.14. The previous versions were 3.13, 3.12, and 2.7."

match_obj = re.search(r'[0-9][0-9]', text)
print(match_obj)

# Using the dot metacharacter to match any character except a newline
pattern_dot = r'3.1.'
matches_dot = re.findall(pattern_dot, text)
print("Matches using dot metacharacter:", matches_dot)

# note that the dot matches any character, so it matches '3.14', '3.13', and '3.12'.
# dot is a special character in regex that matches any single character except a newline.
# for exact dot . character use \. or put it inside a character class [.]
# Using character classes to match specific sets of characters
pattern_class = r'[23]\.\d+'
matches_class = re.findall(pattern_class, text)
print("Matches using character classes:", matches_class)

#  Character classes: are used to define a set of characters to match.
# [abc] - matches any one of the characters a, b, or c.
# [0-9] - matches any digit from 0 to 9.
# [a-z] - matches any lowercase letter from a to z.
# [A-Z] - matches any uppercase letter from A to Z.
# [a-zA-Z] - matches any letter, regardless of case.
# [0-9a-fA-F] - matches any hexadecimal digit.
# \d - matches any digit (equivalent to [0-9]).
# \D - matches any non-digit character (equivalent to [^0-9]).
# \w - matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
# \W - matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_]).
# \s - matches any whitespace character (spaces, tabs, newlines).
# \S - matches any non-whitespace character.
# ^ - when used at the start of a character class, negates the class (e.g., [^a-z] matches any character that is not a lowercase letter).
# Using negated character class to match characters that are not digits
pattern_neg_class = r'[^0-9\s]+'
matches_neg_class = re.findall(pattern_neg_class, text)
print("Matches using negated character class:", matches_neg_class)
# This pattern matches sequences of characters that are not digits or whitespace.
# The output will show the matches found using the dot metacharacter and character classes.
print("Match object using [0-9][0-9]:", match_obj.group() if match_obj else "No match")
print("Matches using dot metacharacter:", matches_dot)
print("Matches using character classes:", matches_class)
print("Matches using negated character class:", matches_neg_class)


