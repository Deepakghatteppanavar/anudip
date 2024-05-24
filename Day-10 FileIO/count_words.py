# Q.2. Write a function in Python to count and display the total number of words in a text file “ABC.txt” 


def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Split the content into words based on whitespace
            words = content.split()
            # Count the number of words
            num_words = len(words)
            # Display the total number of words
            print(f"Total number of words in '{file_name}': {num_words}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
count_words("ABC.txt")