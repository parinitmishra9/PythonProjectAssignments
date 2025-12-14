# Mutability & Immutability
# # Lists are mutable
# # Tuples and Strings are immutable

s1= "Python is fun"
s2 = s1.replace ( "Python", "Java")
print(s1)
print(s2)

print("-----------------------")
print()


l1 = ["Mango", "Orange", "Apple"]
print(id(l1))
l1.append("Banana")
print(l1)
print(id(l1))

print("-----------------------")
print()
