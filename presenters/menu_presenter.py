from entities.shape_type import ShapeType
from models.brush_model import BrushModel
from proxies.canvas_proxy import CanvasProxy
from views.menu_view import MenuView


class MenuPresenter:
    def __init__(self, menu_view: MenuView, canvas_service: CanvasProxy, brush_model: BrushModel):
        self._menu_view = menu_view
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SAVE_TO_FILE, self._save_to_file)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_POINT_SHAPE, self._set_point_shape)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_LINE_SHAPE, self._set_line_shape)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_SIZE, self._set_size)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_COLOR, self._set_color)
        self._canvas_service = canvas_service
        self._brush_model = brush_model

    def update(self):
        color = self._brush_model.get_color()
        self._menu_view.set_current_color(color)

    def _save_to_file(self, _):
        self._canvas_service.save_to_png()

    def _set_point_shape(self, _):
        self._brush_model.set_shape(ShapeType.POINT)

    def _set_line_shape(self, _):
        self._brush_model.set_shape(ShapeType.LINE)

    def _set_size(self, size: int):
        self._brush_model.set_size(size)

    def _set_color(self, color: str):
        self._brush_model.set_color(color)
        self._menu_view.set_current_color(color)
