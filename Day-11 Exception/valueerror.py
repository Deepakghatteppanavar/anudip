# Q.2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 


def get_integer_input():
    try:
        # Prompt the user to input an integer
        num = int(input("Enter an integer: "))
        print("Input integer:", num)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Example usage:
get_integer_input()

