import numpy as np

# Define quantity array
quantity = np.array([2, 3, 4, 1]) 

# Define price per item array
price_per_item = np.array([10.0, 5.0, 8.0, 12.0])

# Calculate total cost by multiplying quantity by price per item
total_cost = quantity * price_per_item

# Print the total cost of items
print("Total Cost of Items:", total_cost)
