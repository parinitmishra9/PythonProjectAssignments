# Quantifiers in Regular Expressions are special characters that specify how many times a character or group of characters should occur in a string.
import re

# Example string
text = "The rain in Spain stays mainly in the plain."
# Pattern to find 'ain' followed by zero or more characters
pattern = r'ain.*'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or more characters:", matches)
# Pattern to find 'ain' followed by one or more characters
pattern = r'ain.+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by one or more characters:", matches)
# Pattern to find 'ain' followed by exactly two characters
pattern = r'ain..'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by exactly two characters:", matches)
# Pattern to find 'ain' followed by zero or one character
pattern = r'ain.?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or one character:", matches)
# Pattern to find 'ain' followed by two to four characters
pattern = r'ain.{2,4}'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two to four characters:", matches)
# Pattern to find 'ain' followed by two or more characters
pattern = r'ain.{2,}'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two or more characters:", matches)
# Pattern to find 'ain' followed by zero or more characters (non-greedy)
pattern = r'ain.*?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or more characters (non-greedy):", matches)
# Pattern to find 'ain' followed by one or more characters (non-greedy)
pattern = r'ain.+?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by one or more characters (non-greedy):", matches)
# Pattern to find 'ain' followed by two to four characters (non-greedy)
pattern = r'ain.{2,4}?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two to four characters (non-greedy):", matches)
# Pattern to find 'ain' followed by two or more characters (non-greedy)
pattern = r'ain.{2,}?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two or more characters (non-greedy):", matches)
# Pattern to find 'ain' followed by zero or more whitespace characters
pattern = r'ain\s*'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or more whitespace characters:", matches)
# Pattern to find 'ain' followed by one or more whitespace characters
pattern = r'ain\s+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by one or more whitespace characters:", matches)
# Pattern to find 'ain' followed by zero or one whitespace character
pattern = r'ain\s?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or one whitespace character:", matches)
# Pattern to find 'ain' followed by two to four whitespace characters
pattern = r'ain\s{2,4}'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two to four whitespace characters:", matches)
# Pattern to find 'ain' followed by two or more whitespace characters
pattern = r'ain\s{2,}'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by two or more whitespace characters:", matches)
# Pattern to find 'ain' followed by zero or more digits
pattern = r'ain\d*'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or more digits:", matches)
# Pattern to find 'ain' followed by one or more digits
pattern = r'ain\d+'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by one or more digits:", matches)
# Pattern to find 'ain' followed by zero or one digit
pattern = r'ain\d?'
# Find all matches
matches = re.findall(pattern, text)
print("Matches for 'ain' followed by zero or one digit:", matches)
