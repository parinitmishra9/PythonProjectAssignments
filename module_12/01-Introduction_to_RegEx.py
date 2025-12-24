# Introduction to Regular Expression (RegEx) in Python -> re module
import re

# Sample text
text = "The current Python version is 3.14. The previous versions were 3.13, 3.12, and 2.7."

print("Python" in text)
print("Java" in text)

print(text.find("3.14"))

# search() method to find the first occurrence of a pattern -> search(regex, string): returns a match object or None
match = re.search(r'3\.\d+', text)
if match:
    print("Found version using search():", match.group())
    print(match)
    print(text[30:34])  # Slicing the text to show the matched part


# Using re module to find all versions in the text
pattern = r'\d+\.\d+'
versions = re.findall(pattern, text)
print("Found versions:", versions)
