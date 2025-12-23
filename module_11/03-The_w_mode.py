# The w mode:
# The 'w' mode in Python is used to open a file for writing. If the file already exists, it will be truncated (emptied) before writing. If the file does not exist, a new file will be created.
# Note:
# 1. Using 'w' mode will overwrite the existing content of the file.
# 2. If you want to append to a file without deleting its existing content, use the 'a' mode instead.
# Example of using 'w' mode to write to a file:
# Open a file in write mode
with open('example_wmode.txt', 'w') as file:
    # Write some text to the file
    file.write('Hello, World!\n')
    file.write('This is an example of using the w mode in Python.\n')
# The file 'example_wmode.txt' will now contain the above two lines of text.
# If you open the same file again in 'w' mode, it will overwrite the existing content:
with open('example_wmode.txt', 'w') as file:
    file.write('This will overwrite the previous content.\n')
# Now, 'example_wmode.txt' will only contain the new line of text.
# To verify the content of the file, you can read it back:
with open('example_wmode.txt', 'r') as file:
    content = file.read()
    print(content)
# Output:
# This will overwrite the previous content.
