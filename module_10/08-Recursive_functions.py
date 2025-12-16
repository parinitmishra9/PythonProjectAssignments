# Recursive functions are functions that call themselves in order to solve a problem.
# They are often used for problems that can be broken down into smaller, similar subproblems.
# A recursive function typically has two main components: a base case and a recursive case.
# The base case is the condition under which the function stops calling itself, preventing infinite recursion.
# The recursive case is where the function calls itself with modified arguments to work towards the base case.
# Here is an example of a simple recursive function that calculates the factorial of a number:
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
# Example usage:
print(factorial(5))  # Output: 120
# Another example is a recursive function to compute the nth Fibonacci number:
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of the two preceding Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
print(fibonacci(6))  # Output: 8
# Recursive functions can be very powerful, but they can also lead to performance issues if not implemented carefully.
# For example, the naive Fibonacci function has exponential time complexity due to repeated calculations.
# To optimize recursive functions, techniques such as memoization or converting to iterative solutions can be used.
# Here is an optimized version of the Fibonacci function using memoization:
def fibonacci_memo(n, memo={}):
    # Check if the value is already computed
    if n in memo:
        return memo[n]
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case with memoization
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# Example usage:
print(fibonacci_memo(50))  # Output: 12586269025
# In summary, recursive functions are a useful tool for solving problems that can be defined in terms of smaller subproblems.
# They require careful design to ensure they have a proper base case and avoid excessive computation.
# With optimizations like memoization, they can be made efficient for larger inputs.

