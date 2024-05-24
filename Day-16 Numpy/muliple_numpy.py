# Q. 2. Convert the below list into a numpy array then display the array then display the first and last 
#       index and then multiply each element by 2 and display the result.
#       Input: my_list = [1, 2, 3, 4, 5]



import numpy as np

#input given input
my_list = [1, 2, 3, 4, 5]

#coverting list to array
new_list = np.array(my_list)

#print statement
print("Given list can be coverted : ",new_list)

# Accessing first item in the list
first_list = np.array(my_list[0])
print("First element of the given list is : " ,first_list)

# Accessing last item in the list
last_item = np.array(my_list[-1])
print("Last element of the given list is : " ,last_item)

#Multiple of 2 with all elements in array
print("multiply each element by 2 and  the result will be :" , new_list * 2)
