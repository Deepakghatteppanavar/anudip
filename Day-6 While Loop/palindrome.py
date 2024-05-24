# Q.2. Write a python program to check whether a number is palindrome or not? 

def is_palindrome(num):
    # Store the original number
    original_num = num
    # Initialize a variable to store the reversed number
    reversed_num = 0
    # Reversing the number
    while num > 0:
        # Extract the last digit of the number
        digit = num % 10
        # Append the digit to the reversed number
        reversed_num = (reversed_num * 10) + digit
        # Remove the last digit from the number
        num = num // 10
    # Check if the original number is equal to its reversed form
    return original_num == reversed_num

# Test the function
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")