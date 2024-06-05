import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the monthly sales data into a 2D array with 3 columns representing quarters
quarterly_sales = monthly_sales.reshape(-1, 3)

# Print each quarter separately
for i, quarter in enumerate(quarterly_sales, start=1):
    print(f"Quarter {i} Sales Data (in thousands of dollars):")
    print(quarter)
