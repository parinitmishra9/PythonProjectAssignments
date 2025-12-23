# Creating files in Python:
# You can create files in Python using the built-in open() function with the 'w' (write) or 'x' (exclusive creation) mode.
# The 'w' mode will create a new file or overwrite an existing file, while the 'x' mode will create a new file and raise an error if the file already exists.
# Note:
# Always remember to close the file after you're done working with it to free up system resources.
# Example using 'w' mode:
file_path_w = 'example_w.txt'
with open(file_path_w, 'w') as file_w:
    file_w.write("This is an example file created using 'w' mode.\n")
    file_w.write("This will overwrite the file if it already exists.\n")
print(f"File '{file_path_w}' created using 'w' mode.")
# Example using 'x' mode:
file_path_x = 'example_x.txt'
try:
    with open(file_path_x, 'x') as file_x:
        file_x.write("This is an example file created using 'x' mode.\n")
        file_x.write("This will raise an error if the file already exists.\n")
    print(f"File '{file_path_x}' created using 'x' mode.")
except FileExistsError:
    print(f"File '{file_path_x}' already exists. Cannot create using 'x' mode.")
# In this code, we create two files: one using 'w' mode and another using 'x' mode.
# The first file will be created or overwritten, while the second file will only be created if it does not already exist.
