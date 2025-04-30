'''
Exercise 2: Parameters, but No Return Value
Instructions
In this example, you will write a function that takes two parameters and will display a customized message.

The starting code has a call to a function, happy_birthday, that you will be writing.

Write the function definition for the function, happy_birthday, which takes two parameters, one named age and one named name (1 line of code).

The function should print Happy Birthday <name>! Congratulations on turning <age>! to the user (1 line of code). For example, if you pass the values 22 for age and Nora for name, the program should display Happy Birthday Nora and congratulations on turning 22 years old! The function should not return a value.

Run the program. As it is currently written, it will always display the same message, but it could be modified to accept input instead of always using the same values.

'''


def happy_birthday(age, name):
   print(f"Happy Birthday {name} congratulations on turning {age} years old!")


# Code to call the function
happy_birthday(22, "Nora")