import numpy as np

# Define a Python list
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Define a Python tuple
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert the list to a NumPy array
list_to_array = np.array(my_list)

# Convert the tuple to a NumPy array
tuple_to_array = np.array(my_tuple)

# Print original list and tuple
print("Original Python list:", my_list)
print("Original Python tuple:", my_tuple)

# Print NumPy arrays after conversion
print("NumPy array from list:", list_to_array)
print("NumPy array from tuple:", tuple_to_array)
