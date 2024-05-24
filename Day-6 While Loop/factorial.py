# Q.3. Write a python program finding the factorial of a given number using a while loop. 

# //Code

def factorial(num):
    # Initialize the factorial to 1
    fact = 1
    # Ensure the loop runs until num becomes 0
    while num > 0:
        # Multiply the current factorial value by num
        fact *= num
        # Decrement num by 1 for the next iteration
        num -= 1
    return fact

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial of", number, "is:", result)