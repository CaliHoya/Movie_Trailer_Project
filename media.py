import webbrowser


class Movie():
    """Creates instances of movies with key data and method to play trailer

    Attributes:
        title: A string containing movie title
        storyline: A string containing movie title
        poster_image_url: URL of the movie poster image file
        trailer_youtube_url: URL of movie trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie instance with all relevant movie data"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens movie trailer pop-up"""
        webbrowser.open(self.trailer_youtube_url)
