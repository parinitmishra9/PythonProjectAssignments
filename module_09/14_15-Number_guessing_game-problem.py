# Number guessing game - problem
"""
Create a simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game
if the user never guesses the number, ask them 10 times and then end the game !!
"""

import random
number_to_guess = random.randint(1, 100)
chances = 10
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Please enter your guess: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congrats! You've guessed the number {number_to_guess} correctly in {attempt} attempts!")
        break
else:
    print(f"Sorry, you've used all {chances} attempts. The number was {number_to_guess}. Better luck next time!")