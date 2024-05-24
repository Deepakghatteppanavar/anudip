
# Q.2. Write a Python program to remove duplicate characters of a given string. 


def remove_duplicates(input_string):
    # Use the join() method to join a set of unique characters
    return ''.join(sorted(set(input_string), key=input_string.index))

# Input string
input_string = "String and String Function"

# Call the function to remove duplicates and store the result
result_string = remove_duplicates(input_string)

# Print the result
print("String after removing duplicates:", result_string)
