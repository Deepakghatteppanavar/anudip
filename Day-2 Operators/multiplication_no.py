# Multiplication of Two Numbers
# Without using function
numa = 10
numb = 20
num3 = numa + numb
num4 = numa * numb # using multiplication operator

print("Addition of two numbers is : - ", num3)  # Printing Output using third variable

print("Multiplication of two numbers is : - ", num4)

def multi():
    num1 = int(input("Enter a First value : -"))  # taking input from user
    num2 = int(input("Enter a Second value : - "))

    print("Addition of two numbers is : -", num1 + num2)
    print("Multiplication of two numbers is : - ", num1 * num2)
multi()