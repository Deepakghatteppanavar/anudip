# Q.2 Using input function take two number and then swap the number


# Code:

# creating  a function based program

def swap(num1=None):

    # without using swap function
    # Taking an input

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number "))

    print("Before swapping numbers:- ", num1 ," ",num2)
    # swapping numbers using operators 
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    #print function
    print("After swapping numbers:- ", num1, num2)
swap()