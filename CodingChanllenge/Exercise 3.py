'''
Instructions
In this example, you will create a function to generate a lucky number. By declaring it as a function, this code can be re-used in other parts of the program. By having the definition in one place, it would allow you to change the functionality in many places by changing one line in the function.

Begin by writing the function definition for a get_lucky_number function. Remember, this function should not require any input parameters (one line of code).

The function should then return the value of lucky_num (one line of code). The value has already been loaded; your task is to return the value to the main program.

Run the program. A random number will be generated in the range (1 to 100, as defined in the function). This allows the logic to be written once and re-used many times in the program.

'''

import random

# Insert code here
def get_lucky_number():
  lucky_num = random.randint(1,100)
  # Insert code here
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)