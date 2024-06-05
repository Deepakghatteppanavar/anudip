import numpy as np

# Input list of NumPy arrays
arr_list = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]

# Calculate mean of each array using list comprehension
means = [np.mean(arr) for arr in arr_list]

print("Means of the arrays:", means)
