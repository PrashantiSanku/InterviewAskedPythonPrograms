'''
Coding challenge: Odd number
Your task:
Write a Python program that takes in a list of numbers and iterates for each number and
checks if it is even or odd. Use the provided numbers list as a starting point.
Iterate over the numbers list: Use a for loop to iterate over the provided list (for number in numbers:).
Check even/odd: Use a conditional statement to determine if each number is even or odd.
Display output: Print a message indicating whether the numbers are even or odd.

Tips:
You can use the modulo operator (%) to check if a number is divisible by 2.
If the remainder of the division by 2 is 0, the number is even.
Otherwise, it's odd.

Example input:
numbers = [3, 9, 1, 10, 5, 2, 8]

Expected output:
3 is odd
9 is odd
1 is odd
10 is even
5 is odd
2 is even
8 is even
'''

# List of numbers
numbers = [3, 9, 1, 10, 5, 2, 8]

# Iterate over the list of numbers
for number in numbers:
# Check if the number is even or odd using the modulo operator
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
        