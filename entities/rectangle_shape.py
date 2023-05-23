from entities.base_shape import BaseShape
from entities.shape_type import ShapeType
from utils.vector2 import Vector2


class RectangleShape(BaseShape):
    def __init__(self, _id: int | None, start_position: Vector2, end_position: Vector2):
        super().__init__(ShapeType.RECTANGLE, _id)
        self._start_position = start_position
        self._end_position = end_position

    def get_start_position(self) -> Vector2:
        return self._start_position

    def set_start_position(self, start_position: Vector2) -> None:
        self._start_position = start_position

    def get_end_position(self) -> Vector2:
        return self._end_position

    def set_end_position(self, end_position: Vector2) -> None:
        self._end_position = end_position
