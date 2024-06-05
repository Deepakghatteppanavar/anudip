import numpy as np

# Creating an array of 10 zeros
arr1 = np.zeros(10)
print("Numpy array of 10 zeros:", arr1)

# Creating an array of 10 ones
arr2 = np.ones(10)
print("Numpy array of 10 ones:", arr2)

# Creating an array of 10 fives
arr3 = np.full(10, 5)
print("Numpy array of 10 fives:", arr3)

# Concatenating the arrays
result = np.concatenate([arr1, arr2, arr3])
print("Combined array:", result)
