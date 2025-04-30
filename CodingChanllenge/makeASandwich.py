'''
Functional code challenge: Make a sandwich
Task:
Create a Python function named make_sandwich.

This function should accept the following parameters:

bread_type (a string representing the type of bread)

filling (a string for the main sandwich filling)

cheese (an optional string for the cheese type, defaulting to "none")

toasted (an optional boolean indicating if the sandwich is toasted, defaulting to False)

Inside the function, construct a descriptive sentence about the sandwich being made, incorporating all the provided details.

Have the function return the sentences shown in the Expected Output section below.

Tips:
Remember to use default values for the optional parameters.

Consider using an if statement to handle the case where no cheese is added.

You can use f-strings for convenient string formatting.

Example Input:
make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham")

Expected output:
Making a toasted wheat sandwich with turkey and cheddar cheese.
Making a rye sandwich with ham.
'''


def make_sandwich(bread_type, filling, cheese="none", toasted=False):
    toast_text = "toasted " if toasted else ""
    cheese_text = f" and {cheese} cheese" if cheese.lower() != "none" else ""

    return f"Making a {toast_text}{bread_type} sandwich with {filling}{cheese_text}."


# Example calls
print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))