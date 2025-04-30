# Storing the values in variable num1 and num2
# num1 = 100
# num2 = 50

# Asking the user the values for variables num1 and num2
num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))

# Printing Before Swapping Values
print("Before Swapping Values are: " , num1, "and", num2)

'''
Approach 1 : With third variable to swap

temp = num1
num1 = num2
num2 = temp

'''

# Approach 2: Swap with two Values
num1, num2 = num2, num1



# printing after swapping values
print("After Swapping Values are: " , num1, "and" , num2)

