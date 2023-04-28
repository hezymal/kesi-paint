from models.brush_model import BrushModel
from entities.line_shape import LineShape
from entities.point_shape import PointShape
from entities.shape_type import ShapeType
from proxies.canvas_proxy import CanvasProxy
from utils.vector2 import Vector2
from views.base_view import BaseView


class CanvasView(BaseView):
    EVENT_CHANNEL_START_DRAW = 'START_DRAW'
    EVENT_CHANNEL_MOVE_DRAW = 'MOVE_DRAW'
    EVENT_CHANNEL_END_DRAW = 'END_DRAW'

    def __init__(self, canvas: CanvasProxy):
        super().__init__()
        self._canvas = canvas
        self._canvas.bind('<Button-1>', self._on_left_mouse_down)
        self._canvas.bind('<B1-Motion>', self._on_left_mouse_move)
        self._canvas.bind('<ButtonRelease-1>', self._on_left_mouse_up)

    def draw_brush(self, brush: BrushModel) -> int | None:
        _type = brush.get_shape_type()
        color = brush.get_color()
        size = brush.get_size()

        if _type == ShapeType.POINT:
            # noinspection PyTypeChecker
            shape: PointShape = brush.get_shape()
            x, y = shape.get_position().values()
            self._draw_point(x, y, color, size)
            return None

        elif _type == ShapeType.LINE:
            # noinspection PyTypeChecker
            shape: LineShape = brush.get_shape()
            _id = brush.get_id()
            x1, y1 = shape.get_start_position().values()
            x2, y2 = shape.get_end_position().values()
            _id = self._draw_line(_id, x1, y1, x2, y2, color, size)
            return _id

        else:
            raise Exception('Unknown a shape type: "{}"'.format(_type))

    def _draw_point(self, x: int, y: int, color: str, size: int) -> None:
        if size == 1:
            self._canvas.create_line(x, y, x + 1, y, fill=color)

        else:
            half_size = size // 2
            x1 = x - half_size
            y1 = y - half_size
            x2 = x + half_size
            y2 = y + half_size
            self._canvas.create_oval(x1, y1, x2, y2, fill=color)

    def _draw_line(self, _id: int | None, x1: int, y1: int, x2: int, y2: int, color: str, size: int) -> int:
        if _id is None:
            _id = self._canvas.create_line(x1, y1, x2, y2, fill=color, width=size)
        else:
            self._canvas.set_position(_id, x1, y1, x2, y2)
        return _id

    def _on_left_mouse_down(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_START_DRAW, Vector2(event.x, event.y))

    def _on_left_mouse_move(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_MOVE_DRAW, Vector2(event.x, event.y))

    def _on_left_mouse_up(self, event) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_END_DRAW, Vector2(event.x, event.y))
