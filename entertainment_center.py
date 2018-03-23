import media
import fresh_tomatoes

# add movie listings
black_panther = media.Movie("Black Panther",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                            "Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=x02xX2dv6bQ")

avengers = media.Movie("Avengers: Infinity War",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/"
                       "Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

venom = media.Movie("Venom",
                    "https://upload.wikimedia.org/wikipedia/en/3/3f/"
                    "Venom_official_teaser_poster.jpg",
                    "https://www.youtube.com/watch?v=B1a6U0YBk_w")
antman = media.Movie("Ant-Man and the Wasp",
                     "https://upload.wikimedia.org/wikipedia/en/2/2c/"
                     "Ant-Man_and_the_Wasp_poster.jpg",
                     "https://www.youtube.com/watch?v=P1m76Cz5ZWU")

# create movie catalogue
movies = [black_panther, avengers, venom, antman]

fresh_tomatoes.open_movies_page(movies)
