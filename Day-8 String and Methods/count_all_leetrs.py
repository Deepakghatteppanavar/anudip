
# Q. 1. Write a Python program to Count all letters, digits, and special symbols from the given 
# string Input = “P@#yn26at^&i5ve” 


def count_characters(input_string):
    # Initialize counts for letters, digits, and special symbols
    letters = 0
    digits = 0
    specials = 0

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            letters += 1  # If it's a letter, increment the letter count
        # Check if the character is a digit
        elif char.isdigit():
            digits += 1  # If it's a digit, increment the digit count
        else:
            specials += 1  # If it's neither a letter nor a digit, increment the special symbol count

    # Return the counts for letters, digits, and special symbols
    return letters, digits, specials