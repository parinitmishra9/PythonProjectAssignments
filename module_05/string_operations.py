s1 = "Python is fun"
print(s1)
print(s1[0])
print(s1[-1])
print(len(s1))

print("-----------------------")
print()

language = "Python"
version = "3.14"
print(language + version)

print("-----------------------")
print()

print(language * 3) #In string, '*' is repetition operator

print("-----------------------")
print()

# Membership operation
# in
print("Python" in s1)
print("i" in s1)
print("z" in s1)
print("Java" in s1)

print("-----------------------")
print()

# not in
print("Python" not in s1)
print("i" not in s1)
print("z" not in s1)
print("Java" not in s1)

print("-----------------------")
print()

# Comparison of Strings
print("Python" == "Python")
print("Python " == "Python")

print("-----------------------")
print()

# Removing spaces from a string - strip()
s1 = "    Python   "
s2 = s1.strip()
print(s2)

print(s1.strip() == "Python")

print("-----------------------")
print()


# replace()
s1 = "We are learning Python"
print(s1.replace("Python", "Java"))
print(s1)

print(s1.replace("e", "E"))
print(s1.replace("e", "E", 1))










