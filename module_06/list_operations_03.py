"""
reverse ()
sort()
count()
Membership operation in list
"""

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days_of_week)
# reverse()
days_of_week.reverse()
print(days_of_week)

print("-----------------------")
print()

nums = [4, 9, 0, 1, 2, 8]
print(nums)
# sort()
nums. sort()
print(nums)
nums. sort(reverse=True)
print(nums)

print("-----------------------")
print()

# count()
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: ") )
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

language = ["Python", "Java", "C++", "Python"]
print(f"The list is: {language}")
item_to_count = input("Enter the item to be counted from the above list: ")
c = language.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

print("-----------------------")
print()

# Membership operation in list
# in
print("Python" in language)
print("Javascript" not in language)

print("-----------------------")
print()
