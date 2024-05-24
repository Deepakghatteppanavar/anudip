
# Q.5. A transport company charges the fare according to following table: Distance Charges 1-50 8 Rs./Km 51-100 10 Rs./Km > 100 12 Rs/Km

# //Code 

# Sub Function 
def transport_comapny(distance):   
    
    # if condition to check the every condition
    if distance >= 1 and distance <= 50:
        charges = 8
    elif distance >= 51 and distance <=100:
        charges = 10
    elif distance >= 100:
        charges = 12
    # Counting distance and percentage
    total_charge = distance * charges

    return total_charge
    

# MAin Function

def fun():
    # Taking an input 
    distances = int(input("Enter the distance to apply the chagres accordingly to the kilometres : "))
    
    # Calling the function
    total_charges = transport_comapny(distances)

    # print the result
    print("You have travled" ,distances,"and your total price will be : ", total_charges)

fun()