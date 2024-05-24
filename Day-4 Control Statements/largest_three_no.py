# Q.2. Python Program to Find the Largest Among Three Numbers 

# //Code

# Main Function
def greatestofthree():
    # Taking Inputs
    num1 = 10
    num2 = 20
    num3 = 30

    # checking inputs using if condition

    if(num1 > num2 & num1 > num3):
        print("Greatest of three number is " ,num1)
    elif(num2 > num1 & num2 > num3):
        print("Greatest of three number is ", num2)
    else:
        print("Greatest of three number is ", num3)

greatestofthree()