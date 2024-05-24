# 1. Using input() function take one number from the user and using ternary operatorscode

# Code:

#using Ternary Operator

# creating  a function based program
# Taking a input
num1 = int(input("Enter a Number to check the number is even or odd :--"))
def ternary_operator():
    # Ternary operator comparing the single value
    result = "Even" if num1 % 2 == 0 else "Odd"

    # Print statement
    print(result)

ternary_operator()