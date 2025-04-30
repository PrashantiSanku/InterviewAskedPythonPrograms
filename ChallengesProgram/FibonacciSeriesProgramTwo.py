'''
I want you to create a python script that prints out the first 10 numbers in the Fibonacci sequence.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
 usually starting with 0 and 1. So the sequence starts: 0,1,1,2,3,5,8,….
'''



# Initializing the first two numbers in the fibonacci series
a, b = 0 ,1

# Using the loop to print the first 10 numbers in the sequence
for i in range(10):
    print(a)
    a,b = b , a + b