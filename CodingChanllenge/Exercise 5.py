'''
Instructions
In this example, you will explore the concept of scope.

1. Run the code below and note the error. The first function call, display_color_works(), will successfully run. The second, display_color_failure(), will result in a NameError.

2. There are a few ways to correct this.

     a. One way is to comment out the line calling the display_color_failure. This does not fix the problem, but it avoids the error.

     b. The preferred way is to set the shirt_color outside of the display_color_works function, in the main program, and pass the value to both functions.

     c. A third way is to catch the error using a try/catch block.

     d. A fourth way is to declare the variable as a global variable, but as discussed in an earlier reading, this is considered bad practice.

3. Comment out the call to the display_color_failure function and re-run the program. Verify the error disappears.
'''

def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)

def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
#display_color_failure()

'''
Fix 2: Passing shirt_color as an Argument (Preferred)
def display_color_works(color):
    print("The shirt color is", color)

def display_color_failure(color):
    print("The shirt color is", color)

shirt_color = "blue"  # Declare in main program
display_color_works(shirt_color)
display_color_failure(shirt_color)  # Now it works correctly
'''

'''
Using a Try/Except Block

def display_color_works():
    shirt_color = "blue"
    print("The shirt color is", shirt_color)

def display_color_failure():
    try:
        print("The shirt color is", shirt_color)
    except NameError:
        print("Error: shirt_color is not defined")

display_color_works()
display_color_failure() 
'''

'''
Fix 4: Using a Global Variable (Not Recommended)

shirt_color = "blue"  # Global variable

def display_color_works():
    print("The shirt color is", shirt_color)

def display_color_failure():
    print("The shirt color is", shirt_color)

display_color_works()
display_color_failure()
'''