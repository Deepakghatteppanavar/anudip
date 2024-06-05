import numpy as np

# Define inventory array
inventory = np.array([10, 0, 5, 0, 20, 0])

# Find the indices where inventory is 0
out_of_stock_indices = np.where(inventory == 0)

# Get the products that are out of stock
out_of_stock_products = inventory[out_of_stock_indices]

# Print the values of products that are out of stock (i.e., have a quantity of 0)
print("Products out of stock:", out_of_stock_products)
