# Q.1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 


def read_file(file_name):
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Print the line, removing any trailing newline characters
                print(line.strip())  # strip() removes trailing newline characters
    # Catch FileNotFoundError exception if the file doesn't exist
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
read_file("ABC.txt")