import numpy as np

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Flatten the array
x_odd_flattened = x_odd.flatten()

# Compute the median
median = np.median(x_odd_flattened)

print("Median of the flattened array:", median)
