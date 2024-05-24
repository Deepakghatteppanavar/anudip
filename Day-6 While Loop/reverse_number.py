# q.1. Write a python program to reverse a number using a while loop. 

# //Code 
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    return reversed_num

# Test the function
number = int(input("Enter a number to reverse: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)