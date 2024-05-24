
# Q.4. Write a function display_words() in python to read lines from a text file "ABC.txt", and display those words, which are less than 4 characters.



def display_words(file_name):
    try:
        with open(file_name, 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Split the line into words
                words = line.split()
                # Loop through each word
                for word in words:
                    # Check if the word has less than 4 characters
                    if len(word) < 4:
                        # Display the word
                        print(word)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
display_words("ABC.txt")