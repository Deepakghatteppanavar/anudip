# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius_temperature = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# Print the result
print("Temperature in Fahrenheit:", fahrenheit_temperature)
