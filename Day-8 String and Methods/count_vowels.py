# Q. 4. Write a Python program to count and display the vowels of a given text 



def vowels_count(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    vowels_list = []

    for char in text:
        if char in vowels:
            vowels_count += 1
            vowels_list.append(char)

    
    # Print the list of vowels found, separated by commas
    print("Vowels:", ", ".join(vowels_list))
    # Print the total number of vowels found in the text
    print("Total number of vowels:", vowels_count)

# Given text string
text = "Welcome to Python Training"

# Call the function to count and display vowels
vowels_count(text)