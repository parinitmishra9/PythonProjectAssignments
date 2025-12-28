# The compile function of re module in Python
# The re.compile() function is used to compile a regular expression pattern into a regex object, which can be used for matching using its methods.
# The re.compile() function takes two main arguments: pattern and flags.
# pattern: The regular expression pattern to be compiled (a string).
# flags: Optional. A set of flags that modify the behavior of the regex. Common flags include re.IGNORECASE, re.MULTILINE, and re.DOTALL.
# Example 1: Compiling a simple regex pattern
import re

pattern = r'\d+'  # Pattern to match one or more digits
regex = re.compile(pattern)
text = "There are 42 apples and 7 bananas."
matches = regex.findall(text)
print(matches)  # Output: ['42', '7']

# Example 2: Using flags with re.compile()
pattern = r'hello'
regex = re.compile(pattern, re.IGNORECASE)  # Case-insensitive matching
text = "Hello world! hello everyone!"
matches = regex.findall(text)
print(matches)  # Output: ['Hello', 'hello']

# Example 3: Compiling a regex pattern with groups
pattern = r'(\w+)@(\w+)\.(\w+)'  # Pattern to match email addresses
regex = re.compile(pattern)
text = "Contact us at Email: parinit@outlook.com"
matches = regex.findall(text)
print(matches)  # Output: [('parinit', 'outlook', 'com')]

# Example 4: Using re.compile() with re.MULTILINE flag
pattern = r'^Hello'
regex = re.compile(pattern, re.MULTILINE)
text = """Hello world!
This is a test.
Hello again!"""
matches = regex.findall(text)
print(matches)  # Output: ['Hello', 'Hello']