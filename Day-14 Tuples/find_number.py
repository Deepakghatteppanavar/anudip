
# Q. 1. Write a Python program to find the number of times 4 appears in the tuple. 
#       Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) 



# Define a tuple with multiple elements
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# The count() method returns the number of times the specified value appears in the tuple
occurrences_of_four = tuplex.count(4)

# Print the result
print(f"The number 4 appears {occurrences_of_four} times in the tuple.")
