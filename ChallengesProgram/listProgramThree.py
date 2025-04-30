'''
I want you to create a Python script that creates a list of your five  favourite fruits.
Then, the script should ask the user for their favourite fruit. If their favourite fruit
is in your list, the script should print ‘We both love[fruit]!’. If it’s not in your list,
 the script should print ‘I haven’t tried [fruit] yet. I’ll have to give it a go!’

'''

# Creating a list of favorite fruits
favorite_fruits = ['Apple', 'Orange', 'Banana', 'Kiwi','Mango']

# Asking the user for their favorite fruit
user_fruit = input('What is your favorite fruit ?')

if user_fruit in favorite_fruits:
    print(f"We both love {user_fruit}!")
else:
    print(f"I haven't tried {user_fruit} yet. I’ll have to give it a go!")