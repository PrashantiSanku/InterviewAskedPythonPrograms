'''
I want you to create a Python function that takes a list of numbers as an argument and
returns the sum of all the numbers in the list. Then, your script should ask the user to
input five numbers, one at a time. Add these numbers to list and call your function with
this list as an argument. Finally, print the result.

'''


def sum_numbers(numbers):
    return sum(numbers)

user_numbers = []

for i in range(5):
    number = int(input(f"Enter number #{i+1}: "))
    user_numbers.append(number)

result = sum_numbers(user_numbers)
print(f"The sum of your number is: {result}")
