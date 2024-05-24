# Q.3 Python Program to Check if a Number is Positive, Negative or 0 

# //Code 

# sub function
def postive_negative(number):
    if number > 0:
        print("Number is postive Number")
    elif (number < 0):
        print( "Number0 is negative")
    else:
        print( "Number is zero type" )
    
# main function
def fun():
    numb = int(input("Enter a number to check postive , negative or zero number : "))
    #Calling sub function
    result = postive_negative(numb)
fun()