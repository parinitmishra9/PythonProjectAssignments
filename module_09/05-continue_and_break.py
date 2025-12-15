# continue and break
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    if i == 8:
        break  # Exit the loop when i is 8
    print(i)
# Output will be: 1, 2, 3, 4, 6, 7
# Note: The number 5 is skipped and the loop stops before printing 8
# Explanation:
# - The 'continue' statement skips the current iteration of the loop when i is 5
# - The 'break' statement exits the loop entirely when i is 8
# - Thus, the numbers 1 to 4 are printed, 5 is skipped, and then 6 and 7 are printed before the loop ends
