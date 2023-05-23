from entities.base_shape import BaseShape
from entities.shape_type import ShapeType
from utils.vector2 import Vector2


class SmoothPointShape(BaseShape):
    def __init__(self, _id: int | None, position: Vector2):
        super().__init__(ShapeType.SMOOTH_POINT, _id)
        self._position = position

    def get_position(self) -> Vector2:
        return self._position

    def set_position(self, position: Vector2) -> None:
        self._position = position
