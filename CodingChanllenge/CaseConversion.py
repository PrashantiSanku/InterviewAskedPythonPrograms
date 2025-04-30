'''
String Shenanigans: Fun with Python Built-in String Functions
Exercise 1: String Length and Case Conversion
Instructions:
Start with the provided variables sentence1 and sentence2, which contain the two humorous sentences.
Use the len() function to calculate the number of characters in sentence1 and sentence2
Apply the upper() function to sentence1 to convert all its characters to uppercase.
Apply the lower() function to transform all the characters in sentence2 to lowercase.
Print the results.
'''

sentence1 = "I'm reading a book about anti-gravity. It's impossible to put down!"
sentence2 = "Why don't scientists trust atoms? Because they make up everything!"

# Find the length of each sentence
length_sentence1 = len(sentence1)
length_sentence2 = len(sentence2)

print("Length of sentence 1:", length_sentence1)
print("Length of sentence 2:", length_sentence2)

# Convert case
uppercase_sentence1 = sentence1.upper()
lowercase_sentence2 = sentence2.lower() 

print("Uppercase sentence 1:", uppercase_sentence1)
print("Lowercase sentence 2:", lowercase_sentence2)