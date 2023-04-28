from proxies.menu_proxy import MenuProxy
from views.base_view import BaseView


class MenuView(BaseView):
    EVENT_CHANNEL_SAVE_TO_FILE = 'SAVE_TO_FILE'
    EVENT_CHANNEL_SET_POINT_SHAPE = 'SET_POINT_SHAPE'
    EVENT_CHANNEL_SET_LINE_SHAPE = 'SET_LINE_SHAPE'
    EVENT_CHANNEL_SET_SIZE = 'SET_SIZE'
    EVENT_CHANNEL_SET_COLOR = 'SET_COLOR'

    def __init__(self, menu: MenuProxy):
        super().__init__()
        self._menu = menu
        self._menu.bind_save_to_png_button_click(self._on_save_to_file_button_click)
        self._menu.bind_point_shape_button_click(self._on_point_shape_button_click)
        self._menu.bind_line_shape_button_click(self._on_line_shape_button_click)
        self._menu.bind_size_scale_change(self._on_shape_size_change)
        self._menu.bind_choose_color_button_click(self._on_choose_color_button_click)

    def set_current_color(self, color: str) -> None:
        self._menu.set_current_color(color)

    def _on_save_to_file_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SAVE_TO_FILE, None)

    def _on_point_shape_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_POINT_SHAPE, None)

    def _on_line_shape_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_LINE_SHAPE, None)

    def _on_shape_size_change(self, size: str) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_SIZE, int(size))

    def _on_choose_color_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_COLOR, self._menu.choose_color())
