
# Q.1. Write a Python program to sum all the items in a list. 


# creating a list
list1 = [11, 5, 17, 18, 23]
#using comprehension
total = 0
[total := total + x for x in list1]
print("total sum of elements in list are " ,total)
 
# using sum() function
total = sum(list1)
# printing total value
print("Sum of all elements in given list: ", total)
