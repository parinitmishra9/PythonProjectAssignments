# Substituting the pattern - sub() method in re module
# It is used to replace the occurrences of a pattern with a specified string.
import re

# Example 1: Replacing all occurrences of 'cat' with 'dog'
text1 = "The cat sat on the mat. The cat is very cute."
pattern1 = r'cat'
replacement1 = 'dog'
result1 = re.sub(pattern1, replacement1, text1)
print("Example 1 Result:", result1)
# Output: The dog sat on the mat. The dog is very cute.

# Example 2: Replacing digits with '#'
text2 = "My phone number is 123-456-7890."
pattern2 = r'\d'
replacement2 = '#'
result2 = re.sub(pattern2, replacement2, text2)
print("Example 2 Result:", result2)
# Output: My phone number is ###-###-####.

# Example 3: Replacing whitespace with a single space
text3 = "This    is  a    test."
pattern3 = r'\s+'
replacement3 = ' '
result3 = re.sub(pattern3, replacement3, text3)
print("Example 3 Result:", result3)
# Output: This is a test.

# Example 4: Replacing vowels with '*'
text4 = "Hello World!"
pattern4 = r'[aeiouAEIOU]'
replacement4 = '*'
result4 = re.sub(pattern4, replacement4, text4)
print("Example 4 Result:", result4)
# Output: H*ll* W*rld!

#  count parameter: limiting the number of substitutions
text5 = "one one one one"
pattern5 = r'one'
replacement5 = 'two'
result5 = re.sub(pattern5, replacement5, text5, count=2)
print("Example 5 Result:", result5)
# Output: two two one one

# Example 6: Using a function as the replacement
def uppercase_match(match):
    return match.group(0).upper()
text6 = "hello world"
pattern6 = r'\b\w+\b'
result6 = re.sub(pattern6, uppercase_match, text6)
print("Example 6 Result:", result6)
# Output: HELLO WORLD

# Example 7: Removing HTML tags
text7 = "<p>This is a <b>bold</b> move.</p>"
pattern7 = r'<.*?>'
replacement7 = ''
result7 = re.sub(pattern7, replacement7, text7)
print("Example 7 Result:", result7)
# Output: This is a bold move.

#  flags parameter: using re.IGNORECASE to ignore case
text8 = "Python is fun. python is easy."
pattern8 = r'python'
replacement8 = 'Java'
result8 = re.sub(pattern8, replacement8, text8, flags=re.IGNORECASE)
print("Example 8 Result:", result8)
# Output: Java is fun. Java is easy.

# Replacing multiple patterns using a single sub() call
text9 = "I have a cat, a dog, and a bird."
pattern9 = r'cat|dog|bird'
replacement9 = 'pet'
result9 = re.sub(pattern9, replacement9, text9)
print("Example 9 Result:", result9)
# Output: I have a pet, a pet, and a pet.
