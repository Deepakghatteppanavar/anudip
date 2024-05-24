# Q.1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 


def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage:
dividend = 10
divisor = 0

divide_numbers(dividend, divisor)