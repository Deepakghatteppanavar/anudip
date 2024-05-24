# Q.3. Python program to check if a given number is an Armstrong number 


# //code

def is_armstrong(num):
    # Converting to string
    num_str = str(num)
    num_digits = len(num_str)
    
    # Initialize sum_of_powers
    sum_of_powers = 0
    
    # Calculate sum of digits raised to the power of num_digits
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Return whether the sum_of_powers is equal to the original number
    return sum_of_powers == num

# Number to check
number_to_check = 153
result = is_armstrong(number_to_check)

# Output the result
if result:
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")