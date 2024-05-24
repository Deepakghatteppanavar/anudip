# Q.3 Write a Program to Convert Kilometers to Miles

# code:
# creating  a function based progra
def km_to_miles(num1=None):
    # without using swap function
    # Taking an input
    m = float(input("Enter a kilomter to convert to miles :-"))

    #converting miles formula
    miles = m * 0.62

    print(m," Kilometer is equals to = ",miles,"Miles")

km_to_miles()