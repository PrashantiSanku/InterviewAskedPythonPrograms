'''
I want you to create a Python script that starts with an empty list.
Then, the script should ask the user for their top three favourite movies, one by one,
and add each movie to the list. Once all movies are added, the script should print:
 ‘Your favourite movies are: [movie1],[movie2], and [movie3].’
'''


# Create a Empty List
favorite_movies =[]

# Asking the user for their top three favourite movies and add each movies to the list.
for i in range(3):
    movie = input(f"What's your #{i+1} favourite movie? ")
    favorite_movies.append(movie)

print(f"Your favourite movies are: {favorite_movies[0]}, {favorite_movies[1]}, and {favorite_movies[2]}")