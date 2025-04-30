'''
Functional code challenge: Leveraging for loops
In this exercise, you will utilize a for loop to count the number of times a particular
word occurs in a sentence.
Some starter code has been included for you:
A get_word_count function that takes two arguments: word_to_count and sentence
An example word to be counted and sentence in the following variables:
word_to_count holds the specific word we want to count
sentence holds the sentence string to count the words from

Task:
Create a function with 2 parameters (code is provided)
Split the sentence variable into words using the split() method and assign it to a new words variable.
Create a new variable count and assign it a value of 0.
Loop through the words variable and count all words that are equal to word_to_count.
Print the result in the following format: print(f"The word '{word_to_count}' appears {count} times in the sentence.")

Tips:
You can use the addition assignment operator += to increment the count variable for each occurrence of the word to count (i.e. count += 1).
Example main program:
word_to_count = "happy"
sentence = "In a happy home, a happy heart creates a happy space."
get_word_count(word_to_count, sentence)

Expected output:
The word 'happy' appears 3 times in the sentence.
'''


# Step 1: Starter code: function with 2 parameters: word_to_count and sentence (provided)
def get_word_count(word_to_count, sentence):
    # Step 2: Split the sentence into words
    # HINT: Use a method called split
    words = sentence.split()
    # Step 3: Initialize the count variable
    count = 0

    # Step 4: Use a for loop to iterate over the words and count occurrences
    for word in words:
        if word == word_to_count:
            count += 1

    # Step 5: Print the result
    print(f"The word '{word_to_count}' appears {count} times in the sentence.")


word_to_count = "happy"
sentence = "In a happy home, a happy heart creates a happy space."
# This will call the created function
get_word_count(word_to_count, sentence)