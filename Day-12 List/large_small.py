# Q.2. Write a Python program to get the largest and smallest number from a list without built-in functions. 


list1 = [10,20,5,15,30,25]

#main function
def grestes_smallest(list1):

    #creating variable for large and small elements
    largest = list1[0]
    smallest = list1[0]

    #for loop to traverse the list
    for num in list1:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

#print the largest and smallest number
print("Largest of number is ", grestes_smallest(list1)[0])
print("smallest of number is ", grestes_smallest(list1)[1])
