
# Q.1. Write a Python program to count the occurrences of each word in a given sentence 

# //Code

# main function

def word_occurance(str):

    # Create an empty dictionary named 'counts' to store word frequencies.
    count_word = dict()
    
    # Split the input string 'str' into a list of words using spaces as separators and store it in the 'words' list.
    words = str.split()

    # Iterate through each word in the 'words' list.
    for word in words:
    
     # Check if the word is already in the 'counts' dictionary.
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1

    # Return the 'counts' dictionary, which contains word frequencies.
    return count_word

# Call the word_count function with an input sentence and print the results.
print(word_occurance('To change the overall look of your document. To change the look available in the gallery')) 