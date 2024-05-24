# Q.4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.


# //code

# Initialize sum to 0
total = 0

# Continuously accept numbers until 0 is entered
while True:
    num = float(input("Enter a number (enter 0 to exit): "))
    # If the entered number is 0, break out of the loop
    if num == 0:
        break
    # Add the entered number to the total
    total += num

# Display the sum of all the numbers entered
print("Sum of all the numbers:", total)