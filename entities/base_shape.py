class BaseShape:
    def __init__(self, _type: str):
        self._type = _type

    def get_type(self):
        return self._type

    def set_type(self, _type):
        self._type = _type
