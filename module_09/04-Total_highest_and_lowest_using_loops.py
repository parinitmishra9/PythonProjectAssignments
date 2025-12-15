# Total, highest and lowest using loops
numbers = [23, 45, 12, 67, 34, 89, 2, 78]
total = 0
highest = numbers[0]
lowest = numbers[0]
for number in numbers:
    total += number
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number
print("Total:", total)
# or
print("Total using sum():", sum(numbers))

print("Highest:", highest)
# or
print("Highest using max():", max(numbers))

print("Lowest:", lowest)
# or
print("Lowest using min():", min(numbers))