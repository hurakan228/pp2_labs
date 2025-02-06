#movie.py
def is_high_rated(movie):
    return movie["imdb"] > 5.5

def is_hith_rated_movies(movies):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies) if movies else 0

def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(categor_movies)