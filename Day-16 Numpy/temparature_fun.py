import numpy as np

# Input temperatures array
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

# Find hot days (temperature exceeds 35 degrees Celsius)
hot_days_indices = np.where(temperatures > 35)[0]
hot_days_temperatures = temperatures[hot_days_indices]

# Find cold days (temperature drops below 5 degrees Celsius)
cold_days_indices = np.where(temperatures < 5)[0]
cold_days_temperatures = temperatures[cold_days_indices]

print("\nHot days:")
for day, temp in zip(hot_days_indices, hot_days_temperatures):
    print(f" {day + 1}: {temp}°C")

print("\nCold days:")
for day, temp in zip(cold_days_indices, cold_days_temperatures):
    print(f" {day + 1}: {temp}°C")
