# The compile function in Python
# The compile() function is used to compile source code into a code object that can be executed by the exec() or eval() functions.
# The compile() function takes three arguments: source, filename, and mode.
# source: The source code to be compiled (a string).
# filename: The name of the file from which the code was read (a string).
# mode: The mode in which the code should be compiled. It can be 'exec', 'eval', or 'single'.
# 'exec': Used for a module or a sequence of statements.
# 'eval': Used for a single expression.
# 'single': Used for a single interactive statement.

# Example 1: Using compile() with exec mode
source_code = """
def greet(name):
    return f'Hello, {name}!'
result = greet('Alice')
"""

code_object = compile(source_code, 'greet_module', 'exec')

print(exec(code_object))  # Output: Hello, Alice!

# Example 2: Using compile() with eval mode
expression = "3 + 5 * 2"
code_object = compile(expression, '<string>', 'eval')
result = eval(code_object)
print(result)  # Output: 13

# Example 3: Using compile() with single mode
single_statement = "print('This is a single statement')"
code_object = compile(single_statement, '<string>', 'single')
exec(code_object)  # Output: This is a single statement
# Note: The compile() function is useful when you need to dynamically execute code that is generated at runtime.
# It allows for better performance by compiling the code once and executing it multiple times.
# Be cautious when using compile() with untrusted input, as it can lead to security vulnerabilities.
# Always validate and sanitize any input before compiling and executing it.

# Example 4: Compiling and executing a loop
loop_code = """for i in range(5):
    print(f'Iteration {i}')
"""
code_object = compile(loop_code, '<string>', 'exec')
exec(code_object)
# Output:
# Iteration 0
# Iteration 1
# Iteration 2
# Iteration 3
# Iteration 4

# Example 5: Compiling a function definition and calling it
function_code = """def add(a, b):
    return a + b
result = add(10, 20)
"""
code_object = compile(function_code, '<string>', 'exec')
exec(code_object)
print(result)  # Output: 30

