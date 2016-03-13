movie_titles = ["Good Will Hunting", "Eternal Sunshine", "Terminator", "Ghost", "Frozen"]
pg_rating = ["R", "R", "R", "PG-13", "PG"]
movie_genre = ["drama", "drama", "action", "drama", "cartoon"]
imdb_rating = [8.3, 8.4, 8.1, 7.0, 7.7]
bechdel_rating = [0, 2, 3, 3, 3]
for movies, rating, genre, imdb, bechdel in zip(movie_titles, pg_rating, movie_genre, imdb_rating, bechdel_rating):
    print "{0}, {1}, {2}, {3}, {4}".format(movies, rating, genre, imdb, bechdel)
