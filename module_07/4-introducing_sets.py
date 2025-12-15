# Sets are non-sequential collection of items
# comma separated elements enclosed within {}

set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# Cannot have indexing with sets as well as slicing is also not allowed
# print(set1[0]) -> not possible

# Length of the set
print(len(set1))


# sets do not allow duplicate elements

l1 = [10, 2.5, 10, 30, 10]
print(l1, type(l1))    # -> [10, 2.5, 10, 30, 10] <class 'list'>
s1 = {10, 2.5,10,30,10}
print(s1, type(s1))  # -> {10, 2.5, 30} <class 'set'>