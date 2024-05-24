# q.4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

# Original list: [1, 1, 2, 3, 4, 4, 5, 1] 

# Length of the first part of the list: 3 

# Splitted the said list into two parts: 

# ([1, 1, 2], [3, 4, 4, 5, 1]) 



def split_list(input_list, length_first_part):
    # Check if the specified length is valid
    if length_first_part >= len(input_list):
        return input_list, []  # Return the whole list as the first part and an empty list as the second part
    else:
        return input_list[:length_first_part], input_list[length_first_part:]  # Split the list based on the specified length

# Given list and length of the first part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3

# Call the function to split the list
first_part, second_part = split_list(original_list, length_first_part)

# Print the original list, length of the first part, and the split result
print("Original list:", original_list)
print("Length of the first part of the list:", length_first_part)
print("Splitted the said list into two parts:")
print((first_part, second_part))
