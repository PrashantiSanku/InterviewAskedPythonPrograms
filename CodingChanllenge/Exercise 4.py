'''
In this example, you will write a function to calculate the discounted total based on whether a user is a member of the discount club or not.

Begin by writing the function definition for the calc_sale_price function. This function will accept two input parameters (one line of code). The first, amount, is a number representing the amount of purchase. The second, member, is a boolean variable representing whether the user is a member (True) or not (False).

Round amount to two decimal places using the built-in function round.

The function should then return the value of amount.

Run the code. The discounted amounts will be displayed.
'''

def calc_sale_price(amount, member):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	# Round amount to two decimal places
	# Insert code here
	round(amount,2)


	# Return amount to the main program
	# Insert code here
	return amount

# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)