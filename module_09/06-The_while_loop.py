# The while loop in Python is used to repeatedly execute a block of code as long as a specified condition is true.
# Syntax:
# while condition:
#     # code block to be executed
# Example 1: Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop
# Example 2: Using while loop with a break statement
number = 0
while True:
    print("Number is:", number)
    number += 1
    if number >= 3:
        break  # Exit the loop when number reaches 3
# Example 3: Using while loop with continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print("i is:", i)
# Example 4: While loop with else clause
n = 0
while n < 3:
    print("n is:", n)
    n += 1
else:
    print("Loop ended, n is now:", n)
# Example 5: Nested while loops
a = 1
while a <= 2:
    b = 1
    while b <= 2:
        print("a:", a, "b:", b)
        b += 1
    a += 1
# Example 6: Infinite loop (commented out to prevent execution)
# while True:
#     print("This will run forever unless interrupted.")
# Note: Be cautious with infinite loops as they can cause your program to hang.
# To stop an infinite loop, you can use Ctrl+C in the terminal or interrupt the kernel in Jupyter notebooks.
# Example 7: Using while loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print("Fruit:", fruits[index])
    index += 1
# Example 8: Using while loop to sum numbers until a condition is met
total = 0
num = 1
while total < 10:
    total += num
    num += 1
print("Total sum is:", total)
# This code demonstrates various uses of the while loop in Python, including basic iteration, using break and continue statements, nested loops, and more.
