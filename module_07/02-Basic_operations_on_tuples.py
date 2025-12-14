"""
concatenation, repetition, membership
count, index
min, max, sum
"""

student_detail1 = (1001, "John")
student_detail2 = (78.5, 91.0, 83.5, 79.5)

print("-----------------------")
print()

# +
student_details = student_detail1 + student_detail2
print(student_details)

print("-----------------------")
print()

# *
t1 = ("Class 5", 5000)
print(t1 * 3)

print("-----------------------")
print()

# in, not in
print(91.0 in student_detail2)
print(91.0 not in student_detail1)

print("-----------------------")
print()

# count
t1 = (10, 4, 1, 9, 0, 3,1)
# tuple. count(element)
print(t1.count(1))

print("-----------------------")
print()

# index
t1 = (10, 4, 1, 9, 0, 3,1)
# tuple. index(element)
print(t1.index(1)) # what is the index of 1 in tuple t1?

print("-----------------------")
print()

# min
print(F"Smallest number: {min(t1)}")
# max
print(F"Biggest number: {max(t1)}")
# sum
print(F"Total: {sum(t1)}")

print("-----------------------")
print()
