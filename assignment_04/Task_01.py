# ask 1: Read a File and Handle Errors

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content successfully read.")
            return content
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to read the file at {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "README.md"
    content = read_file(file_path)
    if content:
        print(content)
