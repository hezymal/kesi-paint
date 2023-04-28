class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def values(self):
        return self.x, self.y

    @staticmethod
    def zero():
        return Vector2(0, 0)
