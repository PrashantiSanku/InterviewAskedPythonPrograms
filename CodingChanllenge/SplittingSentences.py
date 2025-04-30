'''
Exercise 2: Replacing Words and Splitting Sentences
Instructions
Start with the provided variables sentence1 and sentence2, which already contain the two humorous sentences.

Use the replace() function to replace the word "impossible" in sentence1 with the word "challenging".

Use the split() function to divide sentence2 into a list of individual words.

Print the results.
'''

sentence1 = "I'm reading a book about anti-gravity. It's impossible to put down!"
sentence2 = "Why don't scientists trust atoms? Because they make up everything!"

# Replace a word in sentence1
modified_sentence1 = sentence1.replace("impossible", "challenging")
print("Modified sentence 1:", modified_sentence1)

# Split sentence2 into a list of words
words_list = sentence2.split()

print("Words in sentence 2:", words_list)