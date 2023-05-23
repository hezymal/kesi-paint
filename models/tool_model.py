from entities.base_shape import BaseShape
from entities.point_shape import PointShape
from entities.smooth_point_shape import SmoothPointShape
from entities.line_shape import LineShape
from entities.oval_shape import OvalShape
from entities.rectangle_shape import RectangleShape
from entities.shape_type import ShapeType
from entities.tool_type import ToolType
from utils.vector2 import Vector2


class ToolModel:
    def __init__(self):
        self._color_1 = '#000000'
        self._color_2 = '#FFFFFF'
        self._size = 1
        self._tool_type = ToolType.PENCIL
        self._shape = self.create_shape(self._tool_type, None)

    def get_color_1(self) -> str:
        return self._color_1

    def set_color_1(self, color: str) -> None:
        self._color_1 = color

    def get_color_2(self) -> str:
        return self._color_2

    def set_color_2(self, color: str) -> None:
        self._color_2 = color

    def get_shape(self) -> BaseShape:
        return self._shape

    def get_size(self) -> int:
        return self._size

    def set_size(self, size: int) -> None:
        self._size = size

    def get_type(self) -> str:
        return self._tool_type

    def set_type(self, tool_type: str, shape_type: str | None = None) -> None:
        self._shape = self.create_shape(tool_type, shape_type)
        self._tool_type = tool_type

    def start_draw(self, position: Vector2) -> None:
        shape_type = self._shape.get_type()

        if shape_type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.SMOOTH_POINT:
            # noinspection PyTypeChecker
            shape: SmoothPointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_start_position(position)
            shape.set_end_position(position)

        elif shape_type == ShapeType.RECTANGLE:
            # noinspection PyTypeChecker
            shape: RectangleShape = self._shape
            shape.set_start_position(position)
            shape.set_end_position(position)

        elif shape_type == ShapeType.OVAL:
            # noinspection PyTypeChecker
            shape: OvalShape = self._shape
            shape.set_start_position(position)
            shape.set_end_position(position)

        else:
            self.raise_unknown_shape_type_exception(shape_type)

    def start_draw_end(self, shape_id: int) -> None:
        self._shape.set_id(shape_id)

    def move_draw(self, position: Vector2) -> None:
        shape_type = self._shape.get_type()

        if shape_type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.SMOOTH_POINT:
            # noinspection PyTypeChecker
            shape: SmoothPointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_end_position(position)

        elif shape_type == ShapeType.RECTANGLE:
            # noinspection PyTypeChecker
            shape: RectangleShape = self._shape
            shape.set_end_position(position)

        elif shape_type == ShapeType.OVAL:
            # noinspection PyTypeChecker
            shape: OvalShape = self._shape
            shape.set_end_position(position)

        else:
            self.raise_unknown_shape_type_exception(shape_type)

    def end_draw(self, position: Vector2) -> None:
        shape_type = self._shape.get_type()

        if shape_type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.SMOOTH_POINT:
            # noinspection PyTypeChecker
            shape: SmoothPointShape = self._shape
            shape.set_position(position)

        elif shape_type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = self._shape
            shape.set_end_position(position)

        elif shape_type == ShapeType.RECTANGLE:
            # noinspection PyTypeChecker
            shape: RectangleShape = self._shape
            shape.set_end_position(position)

        elif shape_type == ShapeType.OVAL:
            # noinspection PyTypeChecker
            shape: OvalShape = self._shape
            shape.set_end_position(position)

        else:
            self.raise_unknown_shape_type_exception(shape_type)

    def end_draw_end(self) -> None:
        self._shape.set_id(None)

    @staticmethod
    def create_shape(tool_type: str, _shape_type: str | None) -> BaseShape:
        if tool_type == ToolType.PENCIL:
            return PointShape(None, Vector2.zero())

        elif tool_type == ToolType.BRUSH:
            return SmoothPointShape(None, Vector2.zero())

        elif tool_type == ToolType.ERASER:
            return SmoothPointShape(None, Vector2.zero())

        elif tool_type == ToolType.SHAPE:
            return ToolModel.create_shape_by_type(_shape_type)

        else:
            ToolModel.raise_unknown_tool_type_exception(tool_type)

    @staticmethod
    def create_shape_by_type(shape_type: str) -> BaseShape:
        if shape_type == ShapeType.POINT:
            return PointShape(None, Vector2.zero())

        elif shape_type == ShapeType.SMOOTH_POINT:
            return SmoothPointShape(None, Vector2.zero())

        elif shape_type == ShapeType.LINE:
            return LineShape(None, Vector2.zero(), Vector2.zero())

        elif shape_type == ShapeType.RECTANGLE:
            return RectangleShape(None, Vector2.zero(), Vector2.zero())

        elif shape_type == ShapeType.OVAL:
            return OvalShape(None, Vector2.zero(), Vector2.zero())

        else:
            ToolModel.raise_unknown_shape_type_exception(shape_type)

    @staticmethod
    def raise_unknown_tool_type_exception(tool_type: str):
        raise Exception('Unknown a tool type: "{type}"'.format(type=tool_type))

    @staticmethod
    def raise_unknown_shape_type_exception(shape_type: str):
        raise Exception('Unknown a shape type: "{type}"'.format(type=shape_type))
