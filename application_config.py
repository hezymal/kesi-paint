class ApplicationConfig:
    def __init__(self, title, width, height):
        self._title = title
        self._width = width
        self._height = height

    def get_title(self):
        return self._title

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
