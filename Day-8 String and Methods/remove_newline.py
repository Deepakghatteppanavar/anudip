# Q. 2. Write a Python program to remove a newline in Python 



def remove_newline(text):
    new_text = ''
    for char in text:
        if char != '\n':
            new_text += char
    return new_text

# Get input from the user
text_with_newline =  "\nBest \nDeeptech \nPython \nTraining\n" 

print("Before removing new line character: " , text_with_newline)

# Remove newline characters
text_without_newline = remove_newline(text_with_newline)

# Print the result
print("Text without newline character:", text_without_newline)