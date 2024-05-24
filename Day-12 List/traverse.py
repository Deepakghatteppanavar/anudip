
# Q.5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] 


def reverse_traverse_list(input_list):
    # Iterate over the list in reverse order using [::-1]
    for index, value in enumerate(input_list[::-1]):
        # Calculate the original index using the length of the list minus the current index
        original_index = len(input_list) - index - 1
        print(input_list[original_index])  # Print the element from the original list

# Given list
original_list = ['red', 'green', 'white', 'black']

# Call the function to reverse traverse the list
reverse_traverse_list(original_list)
