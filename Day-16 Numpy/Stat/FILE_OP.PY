import numpy as np
import csv

# Step 1: Read the data from the CSV file into a NumPy array
with open('Code\Day-16 Numpy\Stat\house_prices.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = np.array(list(reader), dtype=float)

# Step 2: Calculate the average of house prices
average_price = np.mean(data)

# Step 3: Identify house prices above the average
high_prices = data[data > average_price]

# Step 4: Save the list of high prices to a new CSV file
with open('high_prices.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['High Prices'])
    for price in high_prices:
        writer.writerow([price])

print("Average house price:", average_price)