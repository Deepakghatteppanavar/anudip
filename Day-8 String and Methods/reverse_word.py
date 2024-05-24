# Q. 3. Write a Python program to reverse words in a string 


# Main Function
def reverse_string(text):
    # slicing synatx with along with last charcter
    return text[::-1]

word = 'Deeptech Python Training'
print("Original string is : ", word)

reverse_txt = reverse_string(word)
print("Reverse string is  : " , reverse_txt)