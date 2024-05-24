# Q.3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string



def count_characters(input_string):
    # Initialize counts for uppercase, lowercase, special characters, and digits
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    digit_count = 0

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
        # Check if the character is a digit
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return uppercase_count, lowercase_count, special_count, digit_count

# Input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Call the function to count characters and store the counts
uppercase_count, lowercase_count, special_count, digit_count = count_characters(input_string)

# Print the counts for each category
print("Uppercase count:", uppercase_count)
print("Lowercase count:", lowercase_count)
print("Special character count:", special_count)
print("Numeric value count:", digit_count)