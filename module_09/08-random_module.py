# Random Module Example
import random
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random Integer between 1 and 10: {random_integer}")
# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random Float between 0 and 1: {random_float}")
# Choose a random element from a list
sample_list = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(sample_list)
print(f"Random Choice from list: {random_choice}")
# Shuffle a list randomly
random.shuffle(sample_list)
print(f"Shuffled List: {sample_list}")
# Generate a random sample of 2 elements from the list
random_sample = random.sample(sample_list, 2)
print(f"Random Sample of 2 elements: {random_sample}")
# Set a seed for reproducibility
random.seed(42)
seeded_random_integer = random.randint(1, 10)
print(f"Seeded Random Integer between 1 and 10: {seeded_random_integer}")