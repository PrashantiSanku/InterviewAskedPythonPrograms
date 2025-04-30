'''
So, here’s your challenge: I want you to create a dictionary that stores information about
a book. You can choose any book you like - may be it’s your favourite book or one you’re
reading right now. The dictionary should include the following keys: ‘title’, ’author’,
‘year_published’, and ‘genre’. Make sure to fill in the corresponding values for each key.
But hold on, we’re not finished yet! After you’ve created your dictionary, I want you to
 add another key-value pair to it: ‘is_favorite’, with a boolean value that indicates
 whether the book is your favourite or not.

'''

book= {
    'title': '1984',
    'author': 'George Orwell',
    'year_published': '1949',
    'genre': 'Dystopian'
}

book['is_favorite'] = False
print(book)
