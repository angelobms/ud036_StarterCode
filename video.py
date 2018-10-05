class Video():
    """ This class provides a way to store video related informations"""

    def __init__(self, title, duration):
        """ Constructor method """
        self._title = title
        self._duration = duration

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
