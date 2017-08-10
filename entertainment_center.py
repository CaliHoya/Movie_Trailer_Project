import fresh_tomatoes
import media


# Create multiple instances of the Movie Class for my favorite movies
black_panther = media.Movie("Black Panther",
                        "The Black Panther origin story",
                        "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg", # NOQA
                        "https://www.youtube.com/watch?v=dxWvtMOGAhw")

traffic = media.Movie("Traffic",
                        "A fascinating look into the drug trade from all"
                        " angles",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Traffic2000Poster.jpg", # NOQA
                        "https://www.youtube.com/watch?v=6TetUbh6jrU")

ragnorak = media.Movie("Thor Ragnorak",
                        "Thor battles the goddess of death",
                        "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg", # NOQA
                        "https://www.youtube.com/watch?v=v7MGUNV8MxU")

dark_knight = media.Movie("The Dark Knight",
                        "Batman is faced with an enemy like no other",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", # NOQA
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

la_la_land = media.Movie("La La Land",
                        "An aspiring actress meets a musician as"
                        " they follow their dreams",
                        "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png", # NOQA
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

force_awakens = media.Movie("The Force Awakens",
                        "In the last Star Wars adventure, new heroes rise",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", # NOQA
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")


# Put all instances in a list for use with open_movies_page function
movies = [black_panther, traffic, ragnorak, dark_knight, la_la_land,
          force_awakens]

fresh_tomatoes.open_movies_page(movies)