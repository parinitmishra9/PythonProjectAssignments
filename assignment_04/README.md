# Assignment 4 – Module 5: Files, Exceptions, and Errors in Python

This repository contains Python programs for **Assignment 4** of **Module 5**, focusing on file handling, exceptions, and error handling in Python.

---

## 📌 Task 1: Read a File and Handle Errors

### 🔹 Problem Statement
Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

### 🔹 Description
- The program attempts to open `sample.txt` in read mode.
- If the file exists, each line is printed to the console.
- If the file does not exist, an appropriate error message is displayed using exception handling (`try-except`).

### 🔹 Expected Output

**If the file exists:**
```cmd
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```
**If the file does not exist:**
```cmd
Error: The file 'sample.txt' does not exist.
```

---

## 📌 Task 2: Write and Append Data to a File

### 🔹 Problem Statement
Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

### 🔹 Description
- The program prompts the user for input.
- The entered value is written to `output.txt`.
- Additional text is appended to the same file.
- Finally, the program reads and displays the complete contents of the file.

### 🔹 Expected Output

**If the user enters:**
For example, if the user enters 25, the output should be:

```cmd
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

