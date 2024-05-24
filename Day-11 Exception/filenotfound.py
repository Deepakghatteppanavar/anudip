# Q.3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 


def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print("File contents:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
file_name = input("Enter the file name: ")
open_file(file_name)

