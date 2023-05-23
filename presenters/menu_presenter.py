from entities.shape_type import ShapeType
from entities.tool_type import ToolType
from models.tool_model import ToolModel
from services.canvas_service import CanvasService
from services.tkinter_service import TkinterService
from views.menu_view import MenuView


class MenuPresenter:
    def __init__(self, tkinter_service: TkinterService, menu_view: MenuView, canvas_service: CanvasService,
                 tool_model: ToolModel):
        self._tkinter_service = tkinter_service
        self._menu_view = menu_view
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_NEW_FILE, self._new_file)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_OPEN_FILE, self._open_file)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SAVE_FILE, self._save_file)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_CLOSE_FILE, self._close_application)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_PENCIL_TOOL, self._set_pencil_tool)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_BRUSH_TOOL, self._set_brush_tool)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_ERASER_TOOL, self._set_eraser_tool)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_LINE_PRIMITIVE, self._set_line_primitive)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_RECTANGLE_PRIMITIVE,
                                            self._set_rectangle_primitive)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_OVAL_PRIMITIVE, self._set_oval_primitive)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_SIZE, self._set_size)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_COLOR_1, self._set_color_1)
        self._menu_view.event_bus.subscribe(MenuView.EVENT_CHANNEL_SET_COLOR_2, self._set_color_2)
        self._canvas_service = canvas_service
        self._tool_model = tool_model

    def initialize(self) -> None:
        self._menu_view.set_color_1(self._tool_model.get_color_1())
        self._menu_view.set_color_2(self._tool_model.get_color_2())

    def _new_file(self, _) -> None:
        self._canvas_service.new_file()

    def _open_file(self, _) -> None:
        self._canvas_service.open_file()

    def _save_file(self, _) -> None:
        self._canvas_service.save_file()

    def _close_application(self, _) -> None:
        self._tkinter_service.quit()

    def _set_pencil_tool(self, _) -> None:
        self._tool_model.set_type(ToolType.PENCIL, None)

    def _set_brush_tool(self, _) -> None:
        self._tool_model.set_type(ToolType.BRUSH)

    def _set_eraser_tool(self, _) -> None:
        self._tool_model.set_type(ToolType.ERASER)

    def _set_line_primitive(self, _) -> None:
        self._tool_model.set_type(ToolType.SHAPE, ShapeType.LINE)

    def _set_rectangle_primitive(self, _) -> None:
        self._tool_model.set_type(ToolType.SHAPE, ShapeType.RECTANGLE)

    def _set_oval_primitive(self, _) -> None:
        self._tool_model.set_type(ToolType.SHAPE, ShapeType.OVAL)

    def _set_size(self, size: int) -> None:
        self._tool_model.set_size(size)

    def _set_color_1(self, color: str) -> None:
        self._tool_model.set_color_1(color)
        self._menu_view.set_color_1(color)

    def _set_color_2(self, color: str) -> None:
        self._tool_model.set_color_2(color)
        self._menu_view.set_color_2(color)
