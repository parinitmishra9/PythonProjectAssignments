# Counting substring from a string
# count()
# string.count(substring)
s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(f"Occurrences of {s2} is: {s1.count(s2)}")
print(f"Occurrences of 'e' is: {s1.count("e")}")

print("-----------------------")
print()

# Changing case of a string
# upper(), lower(), title(), capitalize()
s3 = "Python3.14"
print(s3.upper())
print(s3.lower())
print(s1.title())
print(s1.capitalize())

print("-----------------------")
print()

# Starting and ending of a string

s4 = "We are learning Python"

# startswith()
# string.startswith(substring)
print(s4.startswith("Python"))
print(s4.startswith("W"))

# endswith()
# string.endswith(substring)
print(s4.endswith("Python"))
print(s4.endswith("We"))


print("-----------------------")
print()
