from entities.point_shape import PointShape
from entities.smooth_point_shape import SmoothPointShape
from entities.line_shape import LineShape
from entities.oval_shape import OvalShape
from entities.rectangle_shape import RectangleShape
from entities.shape_type import ShapeType
from entities.tool_type import ToolType
from models.tool_model import ToolModel
from services.canvas_service import CanvasService
from utils.vector2 import Vector2
from views.base_view import BaseView


class CanvasView(BaseView):
    EVENT_CHANNEL_START_DRAW = 'START_DRAW'
    EVENT_CHANNEL_MOVE_DRAW = 'MOVE_DRAW'
    EVENT_CHANNEL_END_DRAW = 'END_DRAW'

    def __init__(self, canvas: CanvasService):
        super().__init__()
        self._canvas = canvas
        self._canvas.bind('<Button-1>', self._on_left_mouse_down)
        self._canvas.bind('<B1-Motion>', self._on_left_mouse_move)
        self._canvas.bind('<ButtonRelease-1>', self._on_left_mouse_up)

    def draw(self, tool_model: ToolModel) -> int:
        tool_type = tool_model.get_type()

        if tool_type == ToolType.PENCIL:
            return self._draw_pencil(tool_model)

        elif tool_type == ToolType.BRUSH:
            return self._draw_brush(tool_model)

        elif tool_type == ToolType.ERASER:
            return self._draw_eraser(tool_model)

        elif tool_type == ToolType.SHAPE:
            return self._draw_shape(tool_model)

        else:
            raise Exception('Unknown a tool type: "{type}"'.format(type=tool_type))

    def _draw_pencil(self, tool_model: ToolModel) -> int:
        color = tool_model.get_color_1()
        size = tool_model.get_size()

        # noinspection PyTypeChecker
        shape: PointShape = tool_model.get_shape()
        position = shape.get_position()

        return self._draw_point(position, color, size)

    def _draw_brush(self, tool_model: ToolModel) -> int:
        color = tool_model.get_color_1()
        size = tool_model.get_size()

        # noinspection PyTypeChecker
        shape: SmoothPointShape = tool_model.get_shape()
        position = shape.get_position()

        return self._draw_smooth_point(position, color, size)

    def _draw_eraser(self, tool_model: ToolModel) -> int:
        color = tool_model.get_color_2()
        size = tool_model.get_size()

        # noinspection PyTypeChecker
        shape: SmoothPointShape = tool_model.get_shape()
        position = shape.get_position()

        return self._draw_smooth_point(position, color, size)

    def _draw_shape(self, tool_model: ToolModel) -> int:
        color_1 = tool_model.get_color_1()
        color_2 = tool_model.get_color_2()
        size = tool_model.get_size()

        shape_type = tool_model.get_shape().get_type()
        if shape_type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = tool_model.get_shape()
            return self._draw_line(shape.get_id(), shape.get_start_position(), shape.get_end_position(), color_1, size)

        elif shape_type == ShapeType.RECTANGLE:
            # noinspection PyTypeChecker
            shape: RectangleShape = tool_model.get_shape()
            return self._draw_rectangle(shape.get_id(), shape.get_start_position(), shape.get_end_position(), color_1,
                                        color_2, size)

        elif shape_type == ShapeType.OVAL:
            # noinspection PyTypeChecker
            shape: OvalShape = tool_model.get_shape()
            return self._draw_oval(shape.get_id(), shape.get_start_position(), shape.get_end_position(), color_1,
                                   color_2, size)

        else:
            raise Exception('Unknown a shape type: "{type}"'.format(type=shape_type))

    def _draw_point(self, position: Vector2, color: str, size: int) -> int:
        if size == 1:
            _id = self._canvas.create_line(position.x, position.y, position.x + 1, position.y, fill=color)

        else:
            if size % 2 == 1:
                width = (size - 1) // 2
                points = [
                    position.x,
                    position.y,
                    position.x,
                    position.y - width,
                    position.x + width,
                    position.y,
                    position.x,
                    position.y + width,
                    position.x - width,
                    position.y,
                ]

            else:
                width = size // 2
                points = [
                    position.x - 1 - width,
                    position.y - 1 - width,
                    position.x + width - 1,
                    position.y - 1 - width,
                    position.x + width - 1,
                    position.y + width - 1,
                    position.x - 1 - width,
                    position.y + width - 1,
                ]

            _id = self._canvas.create_polygon(points, fill=color)

        return _id

    def _draw_smooth_point(self, position: Vector2, color: str, size: int) -> int:
        if size == 1:
            _id = self._canvas.create_line(position.x, position.y, position.x + 1, position.y, fill=color)

        else:
            half_size = size // 2
            x1 = position.x - half_size
            y1 = position.y - half_size
            x2 = position.x + half_size
            y2 = position.y + half_size
            _id = self._canvas.create_oval(x1, y1, x2, y2, fill=color)

        return _id

    def _draw_line(self, _id: int | None, start_position: Vector2, end_position: Vector2, color: str, size: int) -> int:
        if _id is None:
            _id = self._canvas.create_line(start_position.x, start_position.y, end_position.x, end_position.y,
                                           fill=color, width=size)
        else:
            self._canvas.set_position(_id, start_position.x, start_position.y, end_position.x, end_position.y)

        return _id

    def _draw_rectangle(self, _id: int | None, start_position: Vector2, end_position: Vector2, color_1: str,
                        color_2: str, size: int) -> int:
        if _id is None:
            _id = self._canvas.create_rectangle(start_position.x, start_position.y, end_position.x, end_position.y,
                                                outline=color_1, fill=color_2, width=size)
        else:
            self._canvas.set_position(_id, start_position.x, start_position.y, end_position.x, end_position.y)

        return _id

    def _draw_oval(self, _id: int | None, start_position: Vector2, end_position: Vector2, color_1: str, color_2: str,
                   size: int) -> int:
        if _id is None:
            _id = self._canvas.create_oval(start_position.x, start_position.y, end_position.x, end_position.y,
                                           outline=color_1, fill=color_2, width=size)
        else:
            self._canvas.set_position(_id, start_position.x, start_position.y, end_position.x, end_position.y)

        return _id

    def _draw_pixel(self, position: Vector2, color: str) -> int:
        return self._canvas.create_line(position.x, position.y, position.x + 1, position.y, fill=color)

    def _on_left_mouse_down(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_START_DRAW, Vector2(event.x, event.y))

    def _on_left_mouse_move(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_MOVE_DRAW, Vector2(event.x, event.y))

    def _on_left_mouse_up(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_END_DRAW, Vector2(event.x, event.y))
