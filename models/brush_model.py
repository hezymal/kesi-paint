from entities.base_shape import BaseShape
from entities.shape_type import ShapeType
from entities.line_shape import LineShape
from entities.point_shape import PointShape
from utils.vector2 import Vector2


class BrushModel:
    def __init__(self):
        self._color = '#000000'
        self._shape = self.create_shape_by_type(ShapeType.POINT)
        self._size = 1
        self._drawing = False
        self._id = None

    def get_color(self):
        return self._color

    def set_color(self, color: str):
        self._color = color

    def get_shape(self) -> BaseShape:
        return self._shape

    def set_shape(self, _type: str):
        self._shape = self.create_shape_by_type(_type)

    def get_shape_type(self):
        return self._shape.get_type()

    def get_id(self) -> int:
        return self._id

    def set_id(self, _id: int | None) -> None:
        self._id = _id

    def start_draw(self, position: Vector2) -> None:
        _type = self._shape.get_type()

        if _type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif _type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_start_position(position)
            shape.set_end_position(position)

        else:
            raise Exception('Unknown a shape type: "{}"'.format(_type))

    def move_draw(self, position: Vector2) -> None:
        _type = self._shape.get_type()

        if _type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif _type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_end_position(position)

        else:
            raise Exception('Unknown a shape type: "{}"'.format(_type))

    def end_draw(self, position: Vector2) -> None:
        _type = self._shape.get_type()

        if _type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif _type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_end_position(position)

        else:
            raise Exception('Unknown a shape type: "{}"'.format(_type))

    def get_size(self) -> int:
        return self._size

    def set_size(self, size: int) -> None:
        self._size = size

    @staticmethod
    def create_shape_by_type(_type: str) -> BaseShape:
        if _type == ShapeType.POINT:
            return PointShape(Vector2.zero())
        elif _type == ShapeType.LINE:
            return LineShape(Vector2.zero(), Vector2.zero())
        else:
            raise Exception('Unknown a shape type: "{}"'.format(_type))
