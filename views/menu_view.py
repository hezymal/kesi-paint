from services.menu_service import MenuService
from views.base_view import BaseView


class MenuView(BaseView):
    EVENT_CHANNEL_NEW_FILE = 'NEW_FILE'
    EVENT_CHANNEL_OPEN_FILE = 'OPEN_FILE'
    EVENT_CHANNEL_SAVE_FILE = 'SAVE_FILE'
    EVENT_CHANNEL_CLOSE_FILE = 'CLOSE_FILE'
    EVENT_CHANNEL_SET_PENCIL_TOOL = 'SET_PENCIL_TOOL'
    EVENT_CHANNEL_SET_BRUSH_TOOL = 'SET_BRUSH_TOOL'
    EVENT_CHANNEL_SET_ERASER_TOOL = 'SET_ERASER_TOOL'
    EVENT_CHANNEL_SET_LINE_PRIMITIVE = 'SET_LINE_PRIMITIVE'
    EVENT_CHANNEL_SET_RECTANGLE_PRIMITIVE = 'SET_RECTANGLE_PRIMITIVE'
    EVENT_CHANNEL_SET_OVAL_PRIMITIVE = 'SET_OVAL_PRIMITIVE'
    EVENT_CHANNEL_SET_SIZE = 'SET_SIZE'
    EVENT_CHANNEL_SET_COLOR_1 = 'SET_COLOR_1'
    EVENT_CHANNEL_SET_COLOR_2 = 'SET_COLOR_2'

    def __init__(self, menu: MenuService):
        super().__init__()
        self._menu = menu
        self._menu.bind_new_file_button_click(self._on_new_file_button_click)
        self._menu.bind_open_file_button_click(self._on_open_file_button_click)
        self._menu.bind_save_file_button_click(self._on_save_file_button_click)
        self._menu.bind_exit_button_click(self._on_close_button_click)
        self._menu.bind_pencil_tool_button_click(self._on_pencil_tool_button_click)
        self._menu.bind_brush_tool_button_click(self._on_brush_tool_button_click)
        self._menu.bind_eraser_tool_button_click(self._on_eraser_tool_button_click)
        self._menu.bind_line_primitive_button_click(self._on_line_primitive_button_click)
        self._menu.bind_rectangle_primitive_button_click(self._on_rectangle_primitive_button_click)
        self._menu.bind_oval_primitive_button_click(self._on_oval_primitive_button_click)
        self._menu.bind_size_scale_change(self._on_shape_size_change)
        self._menu.bind_choose_color_button_1_click(self._on_choose_color_button_1_click)
        self._menu.bind_choose_color_button_2_click(self._on_choose_color_button_2_click)

    def set_color_1(self, color: str) -> None:
        self._menu.set_color_1(color)

    def set_color_2(self, color: str) -> None:
        self._menu.set_color_2(color)

    def _on_new_file_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_NEW_FILE, None)

    def _on_open_file_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_OPEN_FILE, None)

    def _on_save_file_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SAVE_FILE, None)

    def _on_close_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_CLOSE_FILE, None)

    def _on_pencil_tool_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_PENCIL_TOOL, None)

    def _on_brush_tool_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_BRUSH_TOOL, None)

    def _on_eraser_tool_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_ERASER_TOOL, None)

    def _on_line_primitive_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_LINE_PRIMITIVE, None)

    def _on_rectangle_primitive_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_RECTANGLE_PRIMITIVE, None)

    def _on_oval_primitive_button_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_OVAL_PRIMITIVE, None)

    def _on_shape_size_change(self, size: str) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_SIZE, int(size))

    def _on_choose_color_button_1_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_COLOR_1, self._menu.choose_color())

    def _on_choose_color_button_2_click(self) -> None:
        self.event_bus.publish(self.EVENT_CHANNEL_SET_COLOR_2, self._menu.choose_color())
