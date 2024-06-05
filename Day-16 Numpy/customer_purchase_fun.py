import numpy as np

# Input data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Identify customers who made a purchase in the last 30 days
recent_customers_mask = last_purchase_days_ago <= 30
recent_customers = customer_ids[recent_customers_mask]

# Identify customers who haven't made a purchase in the last 30 days
inactive_customers_mask = last_purchase_days_ago > 30
inactive_customers = customer_ids[inactive_customers_mask]

print("Customers who made a purchase in the last 30 days:")
print(recent_customers)

print("\nCustomers who haven't made a purchase in the last 30 days:")
print(inactive_customers)
