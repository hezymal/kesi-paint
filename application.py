from application_config import ApplicationConfig
from presenters.canvas_presenter import CanvasPresenter
from presenters.menu_presenter import MenuPresenter
from models.tool_model import ToolModel
from services.canvas_service import CanvasService
from services.menu_service import MenuService
from services.tkinter_service import TkinterService
from views.canvas_view import CanvasView
from views.menu_view import MenuView
from views.window_view import WindowView


class Application:
    def __init__(self, config: ApplicationConfig):
        self._tkinter_service = TkinterService(config.get_title(), config.get_width(), config.get_height())
        self._menu_service = MenuService(self._tkinter_service)
        self._canvas_service = CanvasService(self._tkinter_service)

        self._brush_model = ToolModel()

        self._window_view = WindowView(self._tkinter_service)
        self._menu_view = MenuView(self._menu_service)
        self._canvas_view = CanvasView(self._canvas_service)

        self._canvas_presenter = CanvasPresenter(self._canvas_view, self._brush_model)
        self._menu_presenter = MenuPresenter(self._tkinter_service, self._menu_view, self._canvas_service,
                                             self._brush_model)

    def run(self) -> None:
        self._menu_presenter.initialize()
        self._window_view.run_loop()
