# Q. 2.Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
 

# Define three dictionaries
dic1 = {1: 10, 2: 20} 
dic2 = {3: 30, 4: 40} 
dic3 = {5: 50, 6: 60}

# Merge the dictionaries using the double asterisks unpacking technique
result = {**dic1, **dic2, **dic3}

# Print the merged result
print("Merged dictionary:", result)

