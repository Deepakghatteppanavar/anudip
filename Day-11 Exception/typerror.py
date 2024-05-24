
# Q.4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical


def get_numerical_inputs():
    try:
        # Prompt the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Input numbers:", num1, "and", num2)
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")

# Example usage:
get_numerical_inputs()
