
# Q. 1. Write a Python program and calculate the mean of the below dictionary. 
#       test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 


# Define a function named mean_of_values that calculates the mean of values in a dictionary
def mean_of_values(test_dict):
    # Initialize a variable sum to store the total sum of values
    sum = 0
    # Iterate through the values of the input dictionary
    for i in test_dict.values():
        # Add each value to the sum variable
        sum += i
        # Calculate the mean by dividing the sum by the number of values in the dictionary
        mean = sum / len(test_dict.values())
    # Return the mean after iterating through all values
    return mean

# Create a dictionary named test_dict with key-value pairs
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Print the original dictionary
print("Given values are " ,test_dict)
# Call the mean_of_values function with the test_dict and print the result
print("Mean of the dictionary values are :", mean_of_values(test_dict))
