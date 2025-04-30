'''
Create a function named ‘add_book’. This function should take three arguments -
an existing library dictionary, a dictionary representing a new book, and the name of
the author of the new book. The function should add the new book to the correct author in
the library dictionary. If the author doesn’t exist in the library yet, the function
should add them.

'''

library = {}

def add_book(library, book, author):
    if author in library:
        library[author].append(book)
    else:
        library[author] = [book]

# Define a book
book = {
    'title': 'Animal Farm',
    'year_published': 1945,
    'genre': 'Dystopian'
}

add_book(library, book, 'George Orwell')
print(library)