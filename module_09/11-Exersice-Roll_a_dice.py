# Exersice - Roll a dice
import random

# Roll the dice and print the result
# """Simulate rolling a six-sided dice and return the result."""
# result = random.randint(1, 6)
# print(f"You rolled a {result}")

print("welcome to the dice roller")

while True:
    choice = input("Press Enter to roll the dice or 'q' to quit: ")
    choice = choice.strip()
    if choice.lower() == 'q':
        print("Thanks for playing! Goodbye.")
        break
    elif choice == '':
        result = random.randint(1, 6)
        print(f"You rolled a {result}")
    else:
        print("Invalid input. Please press Enter to roll the dice or 'q' to quit.")
