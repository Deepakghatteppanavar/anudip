# Q.2. Python program to check if the given string is a palindrome 

# //Code


# Main Function
# Main Function
def is_palindrome():
    # Taking an input
    num = input("Enter a number to check if it is a palindrome or not: ")
    
    # Initialize a flag variable
    is_palindrome = True
    
    # Check each character
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            is_palindrome = False
            break
    
    # Output the result
    if is_palindrome:
        print("Given number is a palindrome")
    else:
        print("It is not a palindrome number")
        
# Call the main function
is_palindrome()