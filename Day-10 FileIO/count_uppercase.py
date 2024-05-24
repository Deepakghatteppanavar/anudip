# Q.3. Write a function in Python to count uppercase character in a text file “ABC.txt” 


def count_uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Initialize a counter for uppercase characters
            uppercase_count = 0
            # Loop through each character in the content
            for char in content:
                # Check if the character is uppercase
                if char.isupper():
                    # Increment the counter if it's uppercase
                    uppercase_count += 1
            # Display the total number of uppercase characters
            print(f"Total number of uppercase characters in '{file_name}': {uppercase_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
count_uppercase("ABC.txt")