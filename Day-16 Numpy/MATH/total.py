import numpy as np

# Define revenue arrays for two categories
category1_revenue = np.array([500, 600, 700, 550]) 
category2_revenue = np.array([450, 700, 800, 600]) 

# Calculate total revenue by adding corresponding elements from both arrays
total_revenue = category1_revenue + category2_revenue

# Print the total revenue
print("Total revenue of the given amounts:", total_revenue)
