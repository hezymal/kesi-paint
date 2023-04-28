from application_config import ApplicationConfig
from presenters.canvas_presenter import CanvasPresenter
from presenters.menu_presenter import MenuPresenter
from models.brush_model import BrushModel
from proxies.tkinter_proxy import TkinterProxy
from views.canvas_view import CanvasView
from views.menu_view import MenuView
from views.window_view import WindowView


class Application:
    def __init__(self, config: ApplicationConfig):
        self._tkinter = TkinterProxy(config.get_title(), config.get_width(), config.get_height())
        self._menu = self._tkinter.create_menu()
        self._canvas = self._tkinter.create_canvas()

        self._brush_model = BrushModel()

        self._window_view = WindowView(self._tkinter)
        self._menu_view = MenuView(self._menu)
        self._canvas_view = CanvasView(self._canvas)

        self._canvas_presenter = CanvasPresenter(self._canvas_view, self._brush_model)
        self._menu_presenter = MenuPresenter(self._menu_view, self._canvas, self._brush_model)

    def run(self) -> None:
        self._menu_presenter.update()
        self._window_view.run_loop()
