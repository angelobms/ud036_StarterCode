import webbrowser
from video import Video


class Movie(Video):
    """ This class provides a way to store movie related informations"""

    def __init__(self, title, duration, storyline, year, director,
                 genre, rated, poster_image_url, trailer_youtube_url):
        """ Constructor method """
        Video.__init__(self, title, duration)
        self._storyline = storyline
        self._year = year
        self._director = director
        self._genre = genre
        self._rated = rated
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url

    def showTrailer(self):
        """ Method for to open the trailer of movie in the web browser """
        webbrowser.open(self.trailer_youtube_url)

    @property
    def storyline(self):
        return self._storyline

    @storyline.setter
    def storyline(self, value):
        self._storyline = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self.director = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def rated(self):
        return self._rated

    @rated.setter
    def rated(self, value):
        self._rated = value

    @property
    def poster_image_url(self):
        return self._poster_image_url

    @poster_image_url.setter
    def poster_image_url(self, value):
        self._poster_image_url = value

    @property
    def trailer_youtube_url(self):
        return self._trailer_youtube_url

    @trailer_youtube_url.setter
    def trailer_youtube_url(self, value):
        self._trailer_youtube_url = value
