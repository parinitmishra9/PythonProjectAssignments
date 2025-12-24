# Task 2: Write and Append Data to a File

def write_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            print(f"Data successfully written to {file_path}.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to write to the file at {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
            print(f"Data successfully appended to {file_path}.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to append to the file at {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "sample.txt"
    data_to_write = "This is the initial content of the file.\n"
    data_to_append = "This content is appended to the file.\n"

    write_to_file(file_path, data_to_write)
    append_to_file(file_path, data_to_append)


