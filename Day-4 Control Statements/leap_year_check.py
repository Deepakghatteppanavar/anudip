# Q.1. Python program to check leap year 



# MAin function

def leap_year():
    # Taking an input
    days = int(input("Enter a days check  whether year is leap year or not : "))
    
    # if else condition to check the year 
    if days == 366:
        print("Given days as ", days, "is a leap year")
    else:
        print( "this number is not leap year")

leap_year()
