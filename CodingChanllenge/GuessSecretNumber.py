'''
Your Task:
You'll create a number guessing game where the computer tries to guess a secret number you
set. The computer will generate random guesses within a range (1 to 10) and continue
guessing until it finds the correct number.

Instructions:
Set your secret_number: Choose a number between 1 and 10 and assign it a variable named secret_number.
Initialize another variable called guess with a value of 0.
Complete the while loop: Add the condition to the while loop to ensure it continues to run as long as the guess is not equal to your secret_number.

Example output:
Guessing: 3
Guessing: 8
Guessing: 1
Guessing: 7
I guessed the right number! It was 7

(Note: This example output is just one possible outcome. The actual output will vary depending on the secret_number and the random guesses.)

'''

import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 6
# Initialize the guess variable here with a value of 0
guess = 0

while guess != secret_number :# Add the while loop condition here
	guess = random.randint(1, 10)
	print(f"Guessing: {guess}")

print(f"I guessed the right number! It was {secret_number}")